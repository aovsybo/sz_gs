from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.conf import settings

from ..models import CallDataInfo, Leads
from ..services.skorozvon import skorozvon_api
from ..services.google_sheets import google_sheets_api

from apscheduler.schedulers.background import BackgroundScheduler


LOCAL_TZ = 3


def get_db_contacts_count_for_interval(start_date, end_date, project_id):
    return (
        Leads.objects
        .filter(addDate__gte=start_date)
        .filter(addDate__lt=end_date)
        .filter(projectId=project_id)
        .count()
    )


def get_db_dialogs_count_for_interval(start_date, end_date, project_id, only_leads=False):
    start_date = datetime.fromtimestamp(start_date)
    end_date = datetime.fromtimestamp(end_date)
    dialogs = (
        CallDataInfo.objects
        .filter(save_date__gte=start_date)
        .filter(save_date__lt=end_date)
        .filter(call_call_project_id=project_id)
        .filter(call_scenario_id__in=settings.SCOROZVON_WORKING_SCENARIO_IDS)

    )
    if only_leads:
        dialogs.filter(call_result_result_id__in=settings.SCOROZVON_WORKING_RESULT_IDS)
    return dialogs.count()


def create_report_for_interval(start_date, end_date, prev_start_date):
    projects_ids = skorozvon_api.get_projects_ids()
    if not projects_ids:
        return
    projects_stat = dict()
    for project_name, project_id in projects_ids.items():
        projects_stat[project_name] = {
            "contacts": get_db_contacts_count_for_interval(
                start_date=start_date,
                end_date=end_date,
                project_id=project_id
            ),
            "dialogs": get_db_dialogs_count_for_interval(
                start_date=start_date,
                end_date=end_date,
                project_id=project_id
            ),
            "leads": get_db_dialogs_count_for_interval(
                start_date=start_date,
                end_date=end_date,
                project_id=project_id,
                only_leads=True,
            ),
        }
    google_sheets_api.create_report_sheet(projects_stat, start_date, end_date, prev_start_date)


def get_month_report():
    today = datetime.today().replace(day=1, hour=LOCAL_TZ, minute=0, second=0, microsecond=0)
    start_date = datetime.timestamp(today)
    end_date = datetime.timestamp(today + relativedelta(months=1))
    prev_start_date = datetime.timestamp(today - relativedelta(months=1))
    create_report_for_interval(start_date, end_date, prev_start_date)


def get_two_weeks_report():
    today = datetime.today().replace(hour=LOCAL_TZ, minute=0, second=0, microsecond=0)
    if today.day > 15:
        two_weeks_ago = today.replace(day=16)
        today = (today + relativedelta(months=1)).replace(day=1)
    else:
        two_weeks_ago = today.replace(day=1)
        today = today.replace(day=16)
    start_date = datetime.timestamp(two_weeks_ago)
    end_date = datetime.timestamp(today)
    prev_start_date = datetime.timestamp(today - relativedelta(months=1))
    create_report_for_interval(start_date, end_date, prev_start_date)


def get_user_stat(start_date: datetime, end_date: datetime, user_id: int):
    return {
        "dialogs": CallDataInfo.objects
            .filter(call_user_id=user_id)
            .filter(save_date__gte=start_date)
            .filter(save_date__lt=end_date)
            .filter(call_duration__gte=15).count(),
        "leads": CallDataInfo.objects
            .filter(call_user_id=user_id)
            .filter(save_date__gte=start_date)
            .filter(save_date__lt=end_date)
            .filter(call_duration__gte=15)
            .filter(call_result_result_id__in=settings.SCOROZVON_WORKING_RESULT_IDS).count()
    }


def get_kpi_report():
    end_time = datetime.now()
    start_time = end_time.replace(hour=0, minute=0, second=0, microsecond=0)
    user_names = google_sheets_api.get_kpi_user_cells().keys()
    users = skorozvon_api.get_users()
    if not users:
        return
    users_stat = dict()
    for user_name in user_names:
        users_stat[user_name] = get_user_stat(
            start_time,
            end_time,
            users[user_name]
        )
    google_sheets_api.create_kpi_report(users_stat)


def update_reports():
    get_two_weeks_report()
    get_month_report()
    get_kpi_report()


def get_intervals(count: int):
    intervals = []
    for i in range(count):
        intervals.append(",".join(
            [str(2 * j * count + i) for j in range(30 // count)]
        ))
    return intervals


def start():
    scheduler = BackgroundScheduler()
    jobs = [
        get_two_weeks_report,
        get_month_report,
        get_kpi_report
    ]
    intervals = get_intervals(len(jobs))
    for i, job in enumerate(jobs):
        scheduler.add_job(job, 'cron', minute=intervals[i])
    scheduler.start()

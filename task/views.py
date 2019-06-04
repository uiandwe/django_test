from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from datetime import datetime, timedelta
import pytz

# Create your views here.
@api_view(['get', 'post'])
def time(request):

    # 현재 시간
    now = datetime.now()
    print(now)

    # 시간 지정 생성
    set_datetime = datetime.strptime('2019-12-31 00:00:00', '%Y-%m-%d %H:%M:%S')
    print(set_datetime)

    # 시간 더하기 뺴기
    before = now - timedelta(hours=7)
    after = now + timedelta(hours=7)
    print(before, after)

    # UTC time
    dt = datetime.utcnow()
    print(dt)

    # iso8601
    # Timezone을 설정
    local_timezone = pytz.timezone('Asia/Seoul')
    local_date = now.replace(tzinfo=pytz.utc).astimezone(local_timezone)
    print(local_date)

    # iso8601 밀리세컨드 제거
    local_date = now.replace(tzinfo=pytz.utc).astimezone(local_timezone).replace(microsecond=0)
    print(local_date)

    # timezone
    tz = local_date.tzinfo
    print(tz)

    # datetime to str
    nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
    print(nowDatetime, type(nowDatetime))

    # datetime to timestamp
    timestamp = now.strftime('%s')
    print(timestamp)

    # timestamp to datetime
    now_datetime = datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    print(now_datetime)

    return Response({"message": "Hello, world!"})

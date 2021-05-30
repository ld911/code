:: 以时间戳创建报告文件夹
set ymd=%date:~0,4%-%date:~5,2%-%date:~8,2%
set hms=%time:~0,2%-%time:~3,2%-%time:~6,2%-%time:~9,2%
set dir=report_%ymd%_%hms%
echo %dt%

:: 执行全部测试用例，报告输出到 report 目录
venv\Scripts\pytest.exe --alluredir=%dir%

:: 展示 report 目录的报告
allure serve %dir%
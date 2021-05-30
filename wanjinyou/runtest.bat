:: 以时间戳创建报告文件夹（好处是每次执行报告都单独存放）
set ymd=%date:~0,4%-%date:~5,2%-%date:~8,2%
set hms=%time:~0,2%-%time:~3,2%-%time:~6,2%-%time:~9,2%
set dir=report_%ymd%_%hms%

:: 使用固定报告目录（好处是所有执行保存存放在一起，可以查看历史情况）
:: 如果不使用固定目录，可以注释下面这句
set dir=report


:: 执行全部测试用例，报告输出到 report 目录
venv\Scripts\pytest.exe --alluredir=%dir%

:: 展示 report 目录的报告
allure serve %dir%
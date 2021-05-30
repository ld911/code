:: 执行全部测试用例，报告输出到 report 目录
venv\Scripts\pytest.exe --alluredir=report

:: 展示 report 目录的报告
allure serve report
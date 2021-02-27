from selenium import webdriver

driver = webdriver.Chrome("C:\minjun\chromedriver")
driver.implicitly_wait(2)
driver.get("https://modoodesigner.com/admin/goods/set_goods_options?provider_seq=1&goods_seq=42&tmp_policy=shop&goodsTax=tax&socialcp_input_type=&package_yn=n&frequentlyopt=0&options_cnt=0&scm_use=N&tmp_seq=20210208190317zzssddsszz&mode=")

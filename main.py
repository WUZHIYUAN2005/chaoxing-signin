# -*- coding: utf-8 -*-
import requests
import time

# ==== 用户自定义配置 ====
cookie = "source=""; fid=18643; _uid=363681549; _d=1749798214413; UID=363681549; vc3=OnbI2pKbVys%2BbQmNkwFsIF%2BPDrZkt7vr1jmSqh3FouUBaL87q0bKufJ1V3ob10ncotJzqYTuwkawt1sFD9Tkpt6Pw93dKzO%2BVOTiVvdg0SIiZ66usVlsyI%2FmIwJQwRsdoMuLWO9WGEiD%2BCAdLMSel5u2J4UZGQocCsJ1Yibga0I%3Da4cd1cb6488a7e8c3fbc67a80d12bb4f; uf=b2d2c93beefa90dcddc1d8b097a4e1148bc60a2d5cd45f2c65d67e55ddb962534b5b5a608bf16b656cf53770b0ce4986dc436c455fddffc2ab5213149d75dadbffcc3e0ecaa21d4fde7746b386401b4fe19f7d2b6faa7d13a5f2f33c8c1f840245bc2cc8f3dac912dfd4860a93fcbeead87281e8abbbaf0732ad7123a1fe60b4577a9aa095a87b2c; cx_p_token=3e92ef1cdf0549b881720caf4af36539; p_auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiIzNjM2ODE1NDkiLCJsb2dpblRpbWUiOjE3NDk3OTgyMTQ0MTQsImV4cCI6MTc1MDQwMzAxNH0.witHsqxlP0EPnT0klDcAtZL6fCHB4LjyAud_vhIy0fA; xxtenc=5b9a7d9f6d4521515d07e2dee50f7d4c; DSSTASH_LOG=C_38-UN_19153-US_363681549-T_1749798214415; jrose=AFDCEFB89D26425248848E5B81B33ADB.ans; spaceFidEnc=29A884B95435768C5BA35ACFC12C4F42; spaceFid=18643; spaceRoleId="""
courseId=248730853
classId=111877218
address = "池州学院池州市贵池区教育园区牧之路199号"
longitude = "117.565412"
latitude = "30.647753"

# ==========[初始化请求头]============
headers = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": cookie
}

session = requests.Session()
session.headers.update(headers)

# ==========【获取签到任务 activeId】==========
def get_active_id(courseId, classId):
    url = f"https://mobilelearn.chaoxing.com/ppt/activeAPI/taskactivelist?courseId={courseId}&classId={classId}"
    resp = session.get(url)
    data = resp.json()
    for item in data.get("activeList", []):
        if item["activeType"] == 2 and item["status"] == 1:
            return item["id"]
    return None

# ==========【执行签到】==========
def do_sign(activeId):
    sign_url = f"https://mobilelearn.chaoxing.com/pptSign/stuSignajax?activeId={activeId}&address={address}&longitude={longitude}&latitude={latitude}"
    resp = session.get(sign_url)
    if "success" in resp.text:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]签到成功")
    else:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]签到失败，返回信息：{resp.text}")

# ==========【主函数】==========
def main():
    print("正在获取签到任务...")
    activeId = get_active_id(courseId, classId)
    if not activeId:
        print("当前没有可用的签到任务")
        return
    print(f"找到签到任务 activeId = {activeId}")
    do_sign(activeId)

if __name__ == "__main__":
    main()
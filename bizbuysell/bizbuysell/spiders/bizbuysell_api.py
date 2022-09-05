import requests

url = "https://www.bizbuysell.com/api/search/BbsSearchListingsLive"

x = 1
payload = {"siteId": 20, "languageId": 10, "categories": [115], "locations": 'null', "excludeLocations": 'null', "askingPriceMax": 2000000, "askingPriceMin": 0, "pageNumber": f'{x}', "keyword": 'null', "cashFlowMin": 0, "cashFlowMax": 0, "grossIncomeMin": 0, "grossIncomeMax": 0, "daysListedAgo": 0, "establishedAfterYear": 0, "listingsWithNoAskingPrice": 0, "homeBasedListings": 0, "includeRealEstateForLease": 0, "listingsWithSellerFinancing": 0, "realEstateIncluded": 0, "showRelocatableListings": 'false', "relatedFranchises": 0, "listingTypeIds": [30,40,80], "designationTypeIds": 'null', "sortList": 'null', "absenteeOwnerListings": 0}
headers = {
    # 'cookie': "_bbs.uid=c5826ba8-6adf-4f54-b473-ea358a2351aa; IpLocation={"IPLocationID":0,"StartingIP":0,"EndingIP":0,"CountryCode":"US","CountryName":null,"StateProvName":null,"CityName":"The Colony","PostalCode":"75056","County":null,"StateProvCode":"TX","Latitude":33.1,"Longitude":-96.88,"Shard":0,"ActualIP":1111863384,"CountryID":1,"RegionID":57}; IpLocationChecked=True; ss_o=true; _initialsource=eyJTb3VyY2VWYWx1ZUlEIjowLCJSZWdpc3RyYXRpb25Tb3VyY2VUeXBlSWQiOjAsIlNvdXJjZVVSTCI6Imh0dHBzJTNhJTJmJTJmd3d3LmJpemJ1eXNlbGwuY29tJTJmbGlzdGluZ3MlMmZQcm9maWxlJTJmZGVmYXVsdC5hc3B4JTNmcSUzZDIwMTM3NDQlMjZscHNoJTNkcmVjZW50bHktcmVub3ZhdGVkLXB1Yi1hbmQtZ3JpbGwtd2l0aC1sb3lhbC1mb2xsb3dpbmctaW4tbnctaG91c3RvbiUyNmxzZW8lM2QxJTI2ZCUzZEwzUmxlR0Z6TFdWemRHRmliR2x6YUdWa0xXSjFjMmx1WlhOelpYTXRabTl5TFhOaGJHVXYiLCJEYXRlVGltZUNyZWF0ZWQiOiJcL0RhdGUoMTY2MTUyNzI3NjQ2MilcLyJ9; _bbs_su_es=eyJTb3VyY2VWYWx1ZUlEIjowLCJSZWdpc3RyYXRpb25Tb3VyY2VUeXBlSWQiOjAsIlNvdXJjZVVSTCI6Imh0dHBzJTNhJTJmJTJmd3d3LmJpemJ1eXNlbGwuY29tJTJmdGV4YXMtZXN0YWJsaXNoZWQtYnVzaW5lc3Nlcy1mb3Itc2FsZSUyZiIsIkRhdGVUaW1lQ3JlYXRlZCI6IlwvRGF0ZSgxNjYxNTI3Mjc2NDYyKVwvIn0=; ASP.NET_SessionId=5uoyg1jmmswby40jpkxodhc4; __AntiXsrfToken=882c88fe77b8440984c7b3bbc345058d; BulletinSrcAdSearch=1; AnyModalSeenCookie=1; ak_bmsc=D4D3E8228C2AE47336C78469D2EC9CBE~000000000000000000000000000000~YAAQSjsvF4Gh5O6CAQAA9+ngBBD5TEcCOrONUDsjzfIFY9HhRjdKj0Be1qgbZnyV8nAOSzOW07JssjPI6Xq/ihQJ735gMeSapubL8SOexnnWq9pa6tZvXjKkdw80i04fjVAwl1DtppBnvC2yie7QVg87Q3Ep7txP8iZ/q9K/M5Ow5A+TztN4p9s/bTDD6McMCUIib2LUNqapkim0s/K+c/ctH26eo5C1bnLeJsJ4UiLWM5fe9wQZdTTRpVBr2nqXc94Udb6s3KEPWdyw0o6HXj41YynQhPmxYre3V1j2ycobEFOqgyOpWFOnorkoRezTFOtxo++CtmEyGcRMJPB4/7PFFpS0HSfDYeJGSTh4YVJ+k1JtTVajiGX9CESgFDueNW3liioFDX1IPZk3ig==; _dssm=1; _track_tkn=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJjNTgyNmJhOC02YWRmLTRmNTQtYjQ3My1lYTM1OGEyMzUxYWEiLCJqdGkiOiI2ZDUwNmFlMS03ZDcwLTRjMDktYWEzYS1kODcxMDNmZjE1YjgiLCJlbnMiOiIyMCIsInN1aWQiOiIiLCJiZnNyIjoiMCIsImRpZCI6IjEwIiwidWFpZCI6IjM4MjY0NCIsInVpcCI6IjY2LjY5LjE3Ni44OCIsImV4cCI6MTY2MjI1MTM1NSwiaXNzIjoiaHR0cHM6Ly9hcGkuYml6YnV5c2VsbC5jb20iLCJhdWQiOiJiaXpidXlzZWxsIn0.n0LULt7Cs7UwsptnSZWYTVZi5u4sgbfaBB97Gd5NQ9w; bm_mi=50125364A239D3A0B6292E0DE006C433~YAAQdzsvF14XwQODAQAAiRkLBRBiyU4zFZOPqkhGxSa9bgg7z7T+eV6IVr8U2QyuRVbZoHOxMXFCIyzhAQS7X2AjZHr5ttbgK4g+FUG/GKsjEQ3cxerxIi7hhBoMOQ92VKKMQ6IurS5jK+c8hzpkF5RL/fPKkBqTjG66KOuEgZOd86zef18Bu9fiDbzVDWaLYsPrCR0tADEpPOkwgvKPL0WaTGnYniv0/0JN6a3zaWLkhcJ1NO+NVAQAiAonS/wryXri5Dwm/JjNuSrdsoaSjEOHoDrYV9E3OwrI3aHCqdHrkvRIKQMTki3N8pGQhaZCcqh6FVABoPgHqOc8H/8QzbNrL542J/YwCLB93/lshVVF06ofcNncr6R+mg==~1; BizAlertsSignupPopupSeen=Sat%2C%2003%20Sep%202022%2020%3A29%3A18%20GMT; bm_sv=C9C3858D22A60A77BA609AADC7A8101A~YAAQSjsvF++x6+6CAQAACN0WBRCGeME9BuIk2BoXtK15xNl6lzpGhX0VguYw1CwQaF7DabC1KyWU+uxoNKURPpZ/womiHY/tBnE/xPJJu9d5Hrt8oCiQi1HUBvmgbxcBosZ9Z9LqyYtagErZVX0L5Ew4vkWiSWLVj9wW57IOX4yNKsBLt2x7OLfOx/gOnWPc37u0cXZ8uN+JV+altXnb5n1nRW+QDytmGr7dsm/iI9scV5YLe5cimdLIjd2rB+YOwqzW0e4=~1",
    'authority': "www.bizbuysell.com",
    'accept': "application/json, text/plain, */*",
    'accept-language': "en-US,en;q=0.9",
    'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOiJjNTgyNmJhOC02YWRmLTRmNTQtYjQ3My1lYTM1OGEyMzUxYWEiLCJqdGkiOiI2ZDUwNmFlMS03ZDcwLTRjMDktYWEzYS1kODcxMDNmZjE1YjgiLCJlbnMiOiIyMCIsInN1aWQiOiIiLCJiZnNyIjoiMCIsImRpZCI6IjEwIiwidWFpZCI6IjM4MjY0NCIsInVpcCI6IjY2LjY5LjE3Ni44OCIsImV4cCI6MTY2MjI1MTM1NSwiaXNzIjoiaHR0cHM6Ly9hcGkuYml6YnV5c2VsbC5jb20iLCJhdWQiOiJiaXpidXlzZWxsIn0.n0LULt7Cs7UwsptnSZWYTVZi5u4sgbfaBB97Gd5NQ9w",
    'content-type': "application/json",
    'origin': "https://www.bizbuysell.com",
    'referer': "https://www.bizbuysell.com/online-and-technology-businesses-for-sale/?q=bHQ9MzAsNDAsODAmcHRvPTIwMDAwMDA%3D",
    # 'sec-ch-ua': "Chromium";v="105", "Not)A; Brand";v="8",
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "Linux",
    'sec-fetch-dest': "empty",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "same-origin",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    'x-correlation-id': "0f7f6d7e-978c-4c88-bb07-09dde8d0d1f6"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

import tls_client

cookies = {
    'vis': '78b0674e5a934189-38f2556465fe5074-0f953bb7a6db761dv1',
    '__stripe_mid': 'ba81b245-d0c0-4478-8b36-65a97ab27d310ed573',
    'woe_id': 'kHUcs5QrWo1O5bnT8B7QK7WeFOoAx0eTFfPA1heTkgk317zrlaKwOONuwKfNAH5IAP6F5AGFN9fe2ILRXFAqOwI98LiD%2FpD9kwm19wG4F3cS%2BEJf61vYWHwpgnE%3D--5%2FBhm931gz%2BurCnK--KDM5459s%2Bg887efsHziDow%3D%3D',
    'last_page': 'https%3A%2F%2Fwww.kickstarter.com%2Fprojects%2Fingramwoodworking%2Frpg-coasters%2Fcomments',
    '__cf_bm': 'jbdeumzcaRTmpm1CpUEtkdWC9vluAv0pKss7hPRkaPg-1753885799-1.0.1.1-GU7wqxcJxjGYPv.AwGcqaPd9pthgIBAtSLxDffSsn4kvyyUvQV7xIuIdoOaFgC.ykK.2Z6o9m6srlORfFLV9fK4MoSfSnqM4JbaIYQpY9g4',
    'ksr_consent': '%7B%22purposes%22%3A%7B%22SaleOfInfo%22%3Afalse%7C%22Analytics%22%3Afalse%7C%22Functional%22%3Afalse%7C%22Advertising%22%3Afalse%7D%7C%22confirmed%22%3Atrue%7C%22prompted%22%3Afalse%7C%22timestamp%22%3A%222025-07-30T14%3A30%3A00.148Z%22%7C%22updated%22%3Afalse%7D',
    'cf_clearance': 'yrqV1ktLpjiIX06XIWTL17cG4lK08i30p3PjIUvsgUU-1753885802-1.2.1.1-.cn8AtEptV.GvLHObMYNYNsyz7N4AsWX0M6dEpE2h_Yag2_S7CT9qyoNbd8eZKhqCBUHsNlIo8a9bkOIJ95Qdd8a9YO.rs98.CalE1kpZqksNJky1nR89HDvCGbs35elkvVTsCELhltM2EcOjAyESn.7edLGsYeq6AlR7lD0IBopxgUgTo2oxQR3bXrz5jbxhAg1nRET0bcZ9WBtb5DqL6YWNZ904ySa6HZRSR5TiU0',
    '__stripe_sid': '7f516831-9582-4508-af25-ff477a10b2ecaa9bba',
    '_ksr_session': 'fwXjpsp9WPljTJPEVNqhwcVtaYJFcElNfilrzweE7L3IOSDHxRE29NJP3qj7qVyqnyxoidpEfdj8otBd06IjzHUNwkVQZ9s5gtyJM924cvgSg7ebrHTlBM5efPtdwmcfZWqThYothAjFCLPVVnzT3DU9sqLgFm%2FPaBtKp0TkWUdfKfMyGTrFX8G629%2FJpJ2%2FEbQyu0PGQfnVzLmwjzH3H%2FPeYFBCCa%2BA7Wof4j62MAYKM7aEQ88GGCZIrT094CoK7cuBUc1GmvvBlRWVe3U%2BAz6kYmg%3D--FVA4Yyw05CPurMMQ--fU9IecipO2sIdzKtM3Fayw%3D%3D',
    'request_time': 'Wed%2C+30+Jul+2025+14%3A30%3A15+-0000',
    'local_offset': '-2363',
}

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://www.kickstarter.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.kickstarter.com/projects/ingramwoodworking/rpg-coasters/comments',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
    'x-csrf-token': 'WN5gXCo_teICRtdydbT3sBjN5lrfI9NHLkaRmxvhC3vdR8CJR5mmoRoCK4afQTAd6nQSnloaw9SFM3tPg9mpjA',
    # 'cookie': 'vis=78b0674e5a934189-38f2556465fe5074-0f953bb7a6db761dv1; __stripe_mid=ba81b245-d0c0-4478-8b36-65a97ab27d310ed573; woe_id=kHUcs5QrWo1O5bnT8B7QK7WeFOoAx0eTFfPA1heTkgk317zrlaKwOONuwKfNAH5IAP6F5AGFN9fe2ILRXFAqOwI98LiD%2FpD9kwm19wG4F3cS%2BEJf61vYWHwpgnE%3D--5%2FBhm931gz%2BurCnK--KDM5459s%2Bg887efsHziDow%3D%3D; last_page=https%3A%2F%2Fwww.kickstarter.com%2Fprojects%2Fingramwoodworking%2Frpg-coasters%2Fcomments; __cf_bm=jbdeumzcaRTmpm1CpUEtkdWC9vluAv0pKss7hPRkaPg-1753885799-1.0.1.1-GU7wqxcJxjGYPv.AwGcqaPd9pthgIBAtSLxDffSsn4kvyyUvQV7xIuIdoOaFgC.ykK.2Z6o9m6srlORfFLV9fK4MoSfSnqM4JbaIYQpY9g4; ksr_consent=%7B%22purposes%22%3A%7B%22SaleOfInfo%22%3Afalse%7C%22Analytics%22%3Afalse%7C%22Functional%22%3Afalse%7C%22Advertising%22%3Afalse%7D%7C%22confirmed%22%3Atrue%7C%22prompted%22%3Afalse%7C%22timestamp%22%3A%222025-07-30T14%3A30%3A00.148Z%22%7C%22updated%22%3Afalse%7D; cf_clearance=yrqV1ktLpjiIX06XIWTL17cG4lK08i30p3PjIUvsgUU-1753885802-1.2.1.1-.cn8AtEptV.GvLHObMYNYNsyz7N4AsWX0M6dEpE2h_Yag2_S7CT9qyoNbd8eZKhqCBUHsNlIo8a9bkOIJ95Qdd8a9YO.rs98.CalE1kpZqksNJky1nR89HDvCGbs35elkvVTsCELhltM2EcOjAyESn.7edLGsYeq6AlR7lD0IBopxgUgTo2oxQR3bXrz5jbxhAg1nRET0bcZ9WBtb5DqL6YWNZ904ySa6HZRSR5TiU0; __stripe_sid=7f516831-9582-4508-af25-ff477a10b2ecaa9bba; _ksr_session=fwXjpsp9WPljTJPEVNqhwcVtaYJFcElNfilrzweE7L3IOSDHxRE29NJP3qj7qVyqnyxoidpEfdj8otBd06IjzHUNwkVQZ9s5gtyJM924cvgSg7ebrHTlBM5efPtdwmcfZWqThYothAjFCLPVVnzT3DU9sqLgFm%2FPaBtKp0TkWUdfKfMyGTrFX8G629%2FJpJ2%2FEbQyu0PGQfnVzLmwjzH3H%2FPeYFBCCa%2BA7Wof4j62MAYKM7aEQ88GGCZIrT094CoK7cuBUc1GmvvBlRWVe3U%2BAz6kYmg%3D--FVA4Yyw05CPurMMQ--fU9IecipO2sIdzKtM3Fayw%3D%3D; request_time=Wed%2C+30+Jul+2025+14%3A30%3A15+-0000; local_offset=-2363',
}

json_data = [
    {
        'operationName': 'CommentsQuery',
        'variables': {
            'commentableId': 'UHJvamVjdC01MzU4NzgyMjM=',
            'nextCursor': None,
            'previousCursor': None,
            'first': 25,
            'last': None,
        },
        'query': 'query CommentsQuery($commentableId: ID!, $nextCursor: String, $previousCursor: String, $replyCursor: String, $first: Int, $last: Int) {\n  commentable: node(id: $commentableId) {\n    id\n    ... on Project {\n      url\n      __typename\n    }\n    ... on Commentable {\n      canComment\n      canCommentSansRestrictions\n      commentsCount\n      projectRelayId\n      canUserRequestUpdate\n      comments(\n        first: $first\n        last: $last\n        after: $nextCursor\n        before: $previousCursor\n      ) {\n        edges {\n          node {\n            ...CommentInfo\n            ...CommentReplies\n            __typename\n          }\n          __typename\n        }\n        pageInfo {\n          startCursor\n          hasNextPage\n          hasPreviousPage\n          endCursor\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  me {\n    id\n    name\n    imageUrl(width: 200)\n    isKsrAdmin\n    url\n    isBlocked\n    userRestrictions {\n      restriction\n      releaseAt\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment CommentInfo on Comment {\n  id\n  body\n  createdAt\n  parentId\n  author {\n    id\n    imageUrl(width: 200)\n    name\n    url\n    isBlocked\n    __typename\n  }\n  removedPerGuidelines\n  authorBadges\n  canReport\n  canDelete\n  canPin\n  hasFlaggings\n  deletedAuthor\n  deleted\n  sustained\n  pinnedAt\n  authorCanceledPledge\n  authorBacking {\n    backingUrl\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment CommentReplies on Comment {\n  replies(last: 3, before: $replyCursor) {\n    totalCount\n    nodes {\n      ...CommentInfo\n      __typename\n    }\n    pageInfo {\n      startCursor\n      hasPreviousPage\n      __typename\n    }\n    __typename\n  }\n  __typename\n}',
    },
]
session = tls_client.Session(
    client_identifier="chrome_112",
    random_tls_extension_order=True
)
response = session.post(
    'https://www.kickstarter.com/graph',
    cookies=cookies,
    headers=headers,
    json=json_data,
    # impersonate='chrome',
    proxy='http://t15386846372432:3tlr1tmn@e241.kdltps.com:15818'
)
print(response.json())

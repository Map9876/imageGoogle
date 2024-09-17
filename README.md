# imageGoogle
## colab selenium 
### 
https://github.com › jpjacobpadilla
The best way to use Selenium in Google Colab Notebooks!
https://github.com/jpjacobpadilla/Google-Colab-Selenium

```
%pip install google-colab-selenium
```

获取网页f12 Network，输出的api链接等
使用 `netLog = driver.get_log("performance")`

如果您想使用Selenium WebDriver的 get_log 方法来捕获性能日志（这通常包含了网络请求信息），您可以使用以下代码。请注意，这个方法在ChromeDriver中是可用的，并且您需要确保 goog:loggingPrefs 设置在Chrome的选项中启用。

下面是一个示例脚本，它使用ChromeDriver来捕获性能日志：
```python
import google_colab_selenium as gs

from selenium import webdriver

# 设置Chrome选项以启用性能日志
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--enable-logging")
chrome_options.add_argument("--log-level=0")
chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

# 初始化WebDriver
driver = gs.Chrome(options=chrome_options)

# 打开网页
driver.get("https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ")

# 等待页面加载，这里我们简单地等待了10秒
driver.implicitly_wait(10)

# 获取性能日志
netLog = driver.get_log("performance")

# 打印或处理日志信息
for entry in netLog:
    print(entry)

# 停止WebDriver
driver.quit()
```

<details>
<summary>查看响应示例：</summary>
  
```
Updated and upgraded APT
Downloaded Google Chrome
Initialized Chromedriver
{'level': 'INFO', 'message': '{"message":{"method":"Network.policyUpdated","params":{}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547454876}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":0,"requestId":"DD2F071B70119E9453BFD51D223E8BC2","timestamp":1923.315636}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547454897}
{'level': 'INFO', 'message': '{"message":{"method":"Page.domContentEventFired","params":{"timestamp":1923.693867}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547454897}
{'level': 'INFO', 'message': '{"message":{"method":"Page.loadEventFired","params":{"timestamp":1923.694502}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547454897}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameStoppedLoading","params":{"frameId":"3E7284AA00690624BB019FC4430314BC"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547454914}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameResized","params":{}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547454914}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameStartedLoading","params":{"frameId":"3E7284AA00690624BB019FC4430314BC"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547454939}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"type":"other"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"VeryHigh","isSameSite":true,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"requestId":"8D7973F50CAAE99C42016BF52D8A5C91","timestamp":1923.738041,"type":"Document","wallTime":1726547454.937749}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547454939}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"connectTiming":{"requestTime":1923.740667},"headers":{"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"en-US,en;q=0.9","Connection":"keep-alive","Host":"www.disneyplus.com","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"none","Sec-Fetch-User":"?1","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"requestId":"8D7973F50CAAE99C42016BF52D8A5C91","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547455294}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":false,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"Cache-Control":"public, max-age=864, s-maxage=900","Connection":"keep-alive","Content-Encoding":"gzip","Content-Length":"72264","Content-Type":"text/html; charset=utf-8","Date":"Tue, 17 Sep 2024 04:30:56 GMT","Server":"nginx/1.23.2","Vary":"Accept-Encoding","X-Powered-By":"Next.js","X-solo-application":"disneyplus-growth-nsb","disable-redirect":"false","language":"en","pathname":"/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","physical-location":"US","region":"jp","url":"/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"headersText":"HTTP/1.1 200 OK\\r\\nContent-Type: text/html; charset=utf-8\\r\\nServer: nginx/1.23.2\\r\\ndisable-redirect: false\\r\\nlanguage: en\\r\\npathname: /series/frieren-beyond-journeys-end/1rlaH8IM0pkQ\\r\\nphysical-location: US\\r\\nregion: jp\\r\\nurl: /en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ\\r\\nX-Powered-By: Next.js\\r\\nContent-Encoding: gzip\\r\\nX-solo-application: disneyplus-growth-nsb\\r\\nContent-Length: 72264\\r\\nCache-Control: public, max-age=864, s-maxage=900\\r\\nDate: Tue, 17 Sep 2024 04:30:56 GMT\\r\\nConnection: keep-alive\\r\\nVary: Accept-Encoding\\r\\n\\r\\n","requestId":"8D7973F50CAAE99C42016BF52D8A5C91","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456132}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","requestId":"8D7973F50CAAE99C42016BF52D8A5C91","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"utf-8","connectionId":50,"connectionReused":false,"encodedDataLength":523,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"Cache-Control":"public, max-age=864, s-maxage=900","Connection":"keep-alive","Content-Encoding":"gzip","Content-Length":"72264","Content-Type":"text/html; charset=utf-8","Date":"Tue, 17 Sep 2024 04:30:56 GMT","Server":"nginx/1.23.2","Vary":"Accept-Encoding","X-Powered-By":"Next.js","X-solo-application":"disneyplus-growth-nsb","disable-redirect":"false","language":"en","pathname":"/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","physical-location":"US","region":"jp","url":"/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"mimeType":"text/html","protocol":"http/1.1","remoteIPAddress":"23.44.150.44","remotePort":443,"responseTime":1.726547456131224e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_256_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disneyplus.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"304502203DA0ABCDDCF9D90E7EBFB94AEF448502C0DEA7BACC8349DB8A9DF6C5F750E1F3022100828F8E1E047B68CEEFF14D16E14C6CA511694F6416E6F22E0406826D48C1640C","status":"Verified","timestamp":1.706023785126e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100F551968BA749E63D16F0664812317C81D0AC9A23E5B39CBE00D40D30D37CA26F0221009F8FBC335F475EB6DE40D9DBCA060451E85E69D6630CED6DBADDE9C7059FB587","status":"Verified","timestamp":1.706023785204e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"304402207333FD209CD40F2B584EA279D545F2E5591EA3549DB9631FCBA7C8738C260B97022069EBF67DE6B3E71127D290A8C8D95EFFAE332E0856CFE996811CA8B22356D97A","status":"Verified","timestamp":1.706023785094e+12}],"subjectName":"*.disneyplus.com","validFrom":1705968000,"validTo":1737590399},"securityState":"secure","status":200,"statusText":"OK","timing":{"connectEnd":352.694,"connectStart":322.153,"dnsEnd":321.941,"dnsStart":0,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":1191.1,"receiveHeadersStart":1190.868,"requestTime":1923.740667,"sendEnd":353.065,"sendStart":352.968,"sslEnd":352.685,"sslStart":332.745,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"timestamp":1924.933362,"type":"Document"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456133}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameNavigated","params":{"frame":{"adFrameStatus":{"adFrameType":"none"},"crossOriginIsolatedContextType":"NotIsolated","domainAndRegistry":"disneyplus.com","gatedAPIFeatures":[],"id":"3E7284AA00690624BB019FC4430314BC","loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","mimeType":"text/html","secureContextType":"Secure","securityOrigin":"https://www.disneyplus.com","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"type":"Navigation"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456140}
{'level': 'INFO', 'message': '{"message":{"method":"Network.policyUpdated","params":{}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456143}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":412368,"encodedDataLength":0,"requestId":"8D7973F50CAAE99C42016BF52D8A5C91","timestamp":1924.942809}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456174}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":7007,"lineNumber":0,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Origin":"https://www.disneyplus.com","Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"High","isLinkPreload":true,"isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://static-assets.bamgrid.com/fonts/inspire/Inspire-Regular.f2199f841165c4ddbafcf177da3ef974.woff2"},"requestId":"9990.2","timestamp":1924.950955,"type":"Font","wallTime":1726547456.150744}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456174}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":7187,"lineNumber":0,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Origin":"https://www.disneyplus.com","Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"High","isLinkPreload":true,"isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://static-assets.bamgrid.com/fonts/inspire/Inspire-Bold.4ff15ddc93445342649194969715b0b5.woff2"},"requestId":"9990.3","timestamp":1924.952699,"type":"Font","wallTime":1726547456.152427}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456174}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":173,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"VeryHigh","isLinkPreload":true,"isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/css/d7217ef32a15aede.css"},"requestId":"9990.4","timestamp":1924.953705,"type":"Stylesheet","wallTime":1726547456.153442}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456174}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":481,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"VeryHigh","isLinkPreload":true,"isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/css/b503c746db7a0c4d.css"},"requestId":"9990.6","timestamp":1924.955081,"type":"Stylesheet","wallTime":1726547456.15481}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456174}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":987,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/webpack-7eb13b5b99357ccb.js"},"requestId":"9990.8","timestamp":1924.956057,"type":"Script","wallTime":1726547456.155781}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":1144,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/framework-7ca4c7590a188064.js"},"requestId":"9990.9","timestamp":1924.956199,"type":"Script","wallTime":1726547456.155913}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":1296,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/main-deda6e05560430d9.js"},"requestId":"9990.10","timestamp":1924.95631,"type":"Script","wallTime":1726547456.156037}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":1454,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/pages/_app-04a807cd96ff1485.js"},"requestId":"9990.11","timestamp":1924.958032,"type":"Script","wallTime":1726547456.157759}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":1605,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/689-1704811563a7aad2.js"},"requestId":"9990.12","timestamp":1924.958204,"type":"Script","wallTime":1726547456.157918}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":1756,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/646-9fd3676fcc0efa42.js"},"requestId":"9990.13","timestamp":1924.958346,"type":"Script","wallTime":1726547456.15806}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":1907,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/182-74c9963345086f4c.js"},"requestId":"9990.14","timestamp":1924.958453,"type":"Script","wallTime":1726547456.158166}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":2058,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/292-02db2ad1e62c2a58.js"},"requestId":"9990.15","timestamp":1924.958549,"type":"Script","wallTime":1726547456.158257}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":2209,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/928-a3fb44f500ddd597.js"},"requestId":"9990.16","timestamp":1924.958662,"type":"Script","wallTime":1726547456.158372}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":2360,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/440-afce561b152fc100.js"},"requestId":"9990.17","timestamp":1924.958751,"type":"Script","wallTime":1726547456.158461}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":2549,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/pages/series/%5BprettyTitle%5D/%5Bslug%5D-b604066ab3641502.js"},"requestId":"9990.18","timestamp":1924.958882,"type":"Script","wallTime":1726547456.158601}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":2709,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/U6_u41-7WVYTgYdDlkjYi/_buildManifest.js"},"requestId":"9990.19","timestamp":1924.958995,"type":"Script","wallTime":1726547456.158737}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":2867,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/U6_u41-7WVYTgYdDlkjYi/_ssgManifest.js"},"requestId":"9990.20","timestamp":1924.959175,"type":"Script","wallTime":1726547456.158886}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":3327,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://static-assets.bamgrid.com/product/disneyplus/images/disney-plus-logo-white.3b4910ec3c8417655f6f0511d5d9244d.svg"},"requestId":"9990.21","timestamp":1924.959286,"type":"Image","wallTime":1726547456.159014}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":146,"lineNumber":275,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Medium","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/ae212c3972ec736bb5793a448280055f9e5921211d4ec316e5e2a472fc797949/original"},"requestId":"9990.22","timestamp":1924.959405,"type":"Image","wallTime":1726547456.159116}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":2789,"lineNumber":741,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Medium","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1/scale?width=768&aspectRatio=1.78&format=webp"},"requestId":"9990.23","timestamp":1924.960675,"type":"Image","wallTime":1726547456.160403}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456176}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":5513,"lineNumber":741,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Medium","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/BD389E7A5EF75EB8CFDAB05C134C97232D6F8C097D0C91C3518096BB56463910/scale?width=768&aspectRatio=1.78&format=webp"},"requestId":"9990.24","timestamp":1924.962092,"type":"Image","wallTime":1726547456.161815}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456176}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":5857,"lineNumber":741,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Medium","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/73EE9910650A52DE775F7E676C539DC8BAC63C4AAF152742A7E5EF1C69429644/scale?width=200&format=webp"},"requestId":"9990.25","timestamp":1924.962259,"type":"Image","wallTime":1726547456.161972}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456176}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":6121,"lineNumber":741,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Medium","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/FAE63AC7AC11C27C949E1856CF188BF09FC20EA52AEA3B65B43C24EEB5F29BFD/scale?width=200&format=webp"},"requestId":"9990.26","timestamp":1924.962374,"type":"Image","wallTime":1726547456.162088}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456176}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":10399,"lineNumber":741,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/14EC756AA7761F4D01AEF0C21A660AD0778F87EF1487F3369CBB2542DD060DC0/scale?width=600&aspectRatio=1.78&format=webp"},"requestId":"9990.29","timestamp":1924.962564,"type":"Image","wallTime":1726547456.162277}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456176}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":10901,"lineNumber":741,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/329B3B6A0FF859ACF4DB56481FB31E660E90B503D0A5FE369F268B4F7E426972/scale?width=600&aspectRatio=1.78&format=webp"},"requestId":"9990.30","timestamp":1924.962681,"type":"Image","wallTime":1726547456.162395}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456176}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":11395,"lineNumber":741,"type":"parser","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/41A0CB7122E8D9A27ABDDCE53F84EFE10647871BCDE35258292713B1CC0C2AF2/scale?width=600&aspectRatio=1.78&format=webp"},"requestId":"9990.31","timestamp":1924.962806,"type":"Image","wallTime":1726547456.162534}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456176}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":243983,"encodedDataLength":0,"requestId":"8D7973F50CAAE99C42016BF52D8A5C91","timestamp":1924.963172}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456176}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameScheduledNavigation","params":{"delay":0,"frameId":"3E7284AA00690624BB019FC4430314BC","reason":"scriptInitiated","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456196}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameRequestedNavigation","params":{"disposition":"currentTab","frameId":"3E7284AA00690624BB019FC4430314BC","reason":"scriptInitiated","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456196}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameStartedLoading","params":{"frameId":"3E7284AA00690624BB019FC4430314BC"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456199}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"stack":{"callFrames":[{"columnNumber":29,"functionName":"langRegionRedirect","lineNumber":247,"scriptId":"7","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},{"columnNumber":46,"functionName":"","lineNumber":263,"scriptId":"7","url":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"}]},"type":"script"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"VeryHigh","isSameSite":true,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"requestId":"A217FBA90DB610A58139EB33E6B16822","timestamp":1925.00135,"type":"Document","wallTime":1726547456.201088}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456201}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameClearedScheduledNavigation","params":{"frameId":"3E7284AA00690624BB019FC4430314BC"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456203}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":72787,"requestId":"8D7973F50CAAE99C42016BF52D8A5C91","timestamp":1924.957062}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456203}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"Allow"},"connectTiming":{"requestTime":1925.002876},"headers":{"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"en-US,en;q=0.9","Connection":"keep-alive","Host":"www.disneyplus.com","Referer":"https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"requestId":"A217FBA90DB610A58139EB33E6B16822","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456203}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1924.959756},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/ae212c3972ec736bb5793a448280055f9e5921211d4ec316e5e2a472fc797949/original",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"u=2, i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.22","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456215}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","age":"15171577","cache-control":"max-age=365000000, immutable","content-length":"19978","content-type":"image/png","date":"Mon, 25 Mar 2024 14:11:20 GMT","etag":"\\"520bd0bca53db0257fc5e9ae95b27aa6\\"","last-modified":"Tue, 12 Mar 2024 03:45:13 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"vqTupWKKfrz5PI06RAR8SD-V8XwzuBIjVFqFHGZJK2Hl3DkKf3vDCQ==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.22","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456224}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","requestId":"9990.22","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":false,"encodedDataLength":373,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","age":"15171577","cache-control":"max-age=365000000, immutable","content-length":"19978","content-type":"image/png","date":"Mon, 25 Mar 2024 14:11:20 GMT","etag":"\\"520bd0bca53db0257fc5e9ae95b27aa6\\"","last-modified":"Tue, 12 Mar 2024 03:45:13 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"vqTupWKKfrz5PI06RAR8SD-V8XwzuBIjVFqFHGZJK2Hl3DkKf3vDCQ==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"image/png","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547456223982e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":55.03,"connectStart":30.036,"dnsEnd":29.927,"dnsStart":0.302,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":64.655,"receiveHeadersStart":64.507,"requestTime":1924.959756,"sendEnd":55.564,"sendStart":55.285,"sslEnd":55.024,"sslStart":40.605,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/ae212c3972ec736bb5793a448280055f9e5921211d4ec316e5e2a472fc797949/original"},"timestamp":1925.026234,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456227}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":19978,"encodedDataLength":0,"requestId":"9990.22","timestamp":1925.026299}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456227}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":20387,"requestId":"9990.22","timestamp":1925.025653}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456228}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1924.953155},"headers":{":authority":"static-assets.bamgrid.com",":method":"GET",":path":"/fonts/inspire/Inspire-Bold.4ff15ddc93445342649194969715b0b5.woff2",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","origin":"https://www.disneyplus.com","priority":"u=1","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"font","sec-fetch-mode":"cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.3","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456244}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameResized","params":{}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456244}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1924.951708},"headers":{":authority":"static-assets.bamgrid.com",":method":"GET",":path":"/fonts/inspire/Inspire-Regular.f2199f841165c4ddbafcf177da3ef974.woff2",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","origin":"https://www.disneyplus.com","priority":"u=1","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"font","sec-fetch-mode":"cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.2","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456244}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1924.954249},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/css/d7217ef32a15aede.css",":scheme":"https","accept":"text/css,*/*;q=0.1","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"u=0","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"style","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.4","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456246}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1924.955475},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/css/b503c746db7a0c4d.css",":scheme":"https","accept":"text/css,*/*;q=0.1","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"u=0","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"style","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.6","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456246}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","access-control-allow-methods":"HEAD, GET","access-control-allow-origin":"*","access-control-max-age":"3000","age":"9360815","cache-control":"max-age=31536000","content-length":"47404","content-type":"binary/octet-stream","date":"Fri, 31 May 2024 20:17:22 GMT","etag":"\\"4ff15ddc93445342649194969715b0b5\\"","last-modified":"Tue, 14 May 2024 15:02:51 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Origin,Access-Control-Request-Headers,Access-Control-Request-Method","via":"1.1 19bcf0769b1328ef147a6af36ae38b82.cloudfront.net (CloudFront)","x-amz-cf-id":"-YQoIYE5LXG5_7d4a29oBVNOCAGDZkoLWmbPHhESlP3fFZkh8vhMxw==","x-amz-cf-pop":"LAX54-P2","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"mHgivmJvrFPL1bt8KLmQabrk3A21esyc","x-cache":"Hit from cloudfront"},"requestId":"9990.3","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456254}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","requestId":"9990.3","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":141,"connectionReused":false,"encodedDataLength":587,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","access-control-allow-methods":"HEAD, GET","access-control-allow-origin":"*","access-control-max-age":"3000","age":"9360815","cache-control":"max-age=31536000","content-length":"47404","content-type":"binary/octet-stream","date":"Fri, 31 May 2024 20:17:22 GMT","etag":"\\"4ff15ddc93445342649194969715b0b5\\"","last-modified":"Tue, 14 May 2024 15:02:51 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Origin,Access-Control-Request-Headers,Access-Control-Request-Method","via":"1.1 19bcf0769b1328ef147a6af36ae38b82.cloudfront.net (CloudFront)","x-amz-cf-id":"-YQoIYE5LXG5_7d4a29oBVNOCAGDZkoLWmbPHhESlP3fFZkh8vhMxw==","x-amz-cf-pop":"LAX54-P2","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"mHgivmJvrFPL1bt8KLmQabrk3A21esyc","x-cache":"Hit from cloudfront"},"mimeType":"binary/octet-stream","protocol":"h2","remoteIPAddress":"3.168.132.100","remotePort":443,"responseTime":1.726547456253331e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":88.671,"connectStart":59.583,"dnsEnd":59.452,"dnsStart":0,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":100.64,"receiveHeadersStart":100.452,"requestTime":1924.953155,"sendEnd":90.091,"sendStart":89.243,"sslEnd":88.663,"sslStart":70.159,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://static-assets.bamgrid.com/fonts/inspire/Inspire-Bold.4ff15ddc93445342649194969715b0b5.woff2"},"timestamp":1925.055086,"type":"Font"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456255}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"521388","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"text/css","date":"Wed, 11 Sep 2024 03:41:09 GMT","etag":"W/\\"91bccef3f66ef49a2c3b4c10f64a4ae1\\"","last-modified":"Wed, 11 Sep 2024 01:08:31 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"0SC7Do3O7v_FZtLLEFvOR4qVjDgnUgaO2S7BXa5kZKOLi709PKtr6Q==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"7v1FKlNNElbUZUeZLFHcLOgB3qrfRqmL","x-cache":"Hit from cloudfront"},"requestId":"9990.4","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456258}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"528184","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"text/css","date":"Wed, 11 Sep 2024 07:28:19 GMT","etag":"W/\\"ac4c71354de0b6914046a44ebadfc3eb\\"","last-modified":"Wed, 04 Sep 2024 02:38:48 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"G7n9yuTGmMpjVG4A8CK_RnFz2XbU27iegOzy5XuuvVocU2wEkaN09A==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"i1iMYDX6RR9tECwvwQkOijolVLr_ntV3","x-cache":"Hit from cloudfront"},"requestId":"9990.6","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456258}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":15779,"encodedDataLength":15797,"requestId":"9990.3","timestamp":1925.056339}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456259}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","requestId":"9990.4","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":false,"encodedDataLength":463,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"521388","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"text/css","date":"Wed, 11 Sep 2024 03:41:09 GMT","etag":"W/\\"91bccef3f66ef49a2c3b4c10f64a4ae1\\"","last-modified":"Wed, 11 Sep 2024 01:08:31 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"0SC7Do3O7v_FZtLLEFvOR4qVjDgnUgaO2S7BXa5kZKOLi709PKtr6Q==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"7v1FKlNNElbUZUeZLFHcLOgB3qrfRqmL","x-cache":"Hit from cloudfront"},"mimeType":"text/css","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456256106e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":91.396,"connectStart":62.011,"dnsEnd":61.813,"dnsStart":0.195,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":102.369,"receiveHeadersStart":102.135,"requestTime":1924.954249,"sendEnd":92.118,"sendStart":91.821,"sslEnd":91.389,"sslStart":72.332,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/css/d7217ef32a15aede.css"},"timestamp":1925.059251,"type":"Stylesheet"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456260}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":59603,"encodedDataLength":0,"requestId":"9990.4","timestamp":1925.059315}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456260}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":0,"encodedDataLength":11625,"requestId":"9990.4","timestamp":1925.060339}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456260}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":12088,"requestId":"9990.4","timestamp":1925.058015}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456260}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","requestId":"9990.6","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":460,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"528184","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"text/css","date":"Wed, 11 Sep 2024 07:28:19 GMT","etag":"W/\\"ac4c71354de0b6914046a44ebadfc3eb\\"","last-modified":"Wed, 04 Sep 2024 02:38:48 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"G7n9yuTGmMpjVG4A8CK_RnFz2XbU27iegOzy5XuuvVocU2wEkaN09A==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"i1iMYDX6RR9tECwvwQkOijolVLr_ntV3","x-cache":"Hit from cloudfront"},"mimeType":"text/css","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456257968e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":103.098,"receiveHeadersStart":102.772,"requestTime":1924.955475,"sendEnd":90.894,"sendStart":90.683,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/css/b503c746db7a0c4d.css"},"timestamp":1925.06075,"type":"Stylesheet"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456262}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":14187,"encodedDataLength":0,"requestId":"9990.6","timestamp":1925.0608}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456262}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":0,"encodedDataLength":2730,"requestId":"9990.6","timestamp":1925.061075}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456262}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":3190,"requestId":"9990.6","timestamp":1925.059542}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456262}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":31625,"encodedDataLength":31661,"requestId":"9990.3","timestamp":1925.063081}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456263}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":48045,"requestId":"9990.3","timestamp":1925.062785}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456263}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","access-control-allow-methods":"HEAD, GET","access-control-allow-origin":"*","access-control-max-age":"3000","age":"10964949","cache-control":"max-age=31536000","content-length":"45768","content-type":"binary/octet-stream","date":"Mon, 13 May 2024 06:41:48 GMT","etag":"\\"f2199f841165c4ddbafcf177da3ef974\\"","last-modified":"Thu, 09 May 2024 18:28:30 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Origin,Access-Control-Request-Headers,Access-Control-Request-Method","via":"1.1 19bcf0769b1328ef147a6af36ae38b82.cloudfront.net (CloudFront)","x-amz-cf-id":"gwff2WSN7GG1qU8avfvY6ptHaGNymVvCwdoLZnLX6g7XEY0v0TwybA==","x-amz-cf-pop":"LAX54-P2","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"dkRm0Wve.r.WDBDln90vy9jv3Zt.YaAn","x-cache":"Hit from cloudfront"},"requestId":"9990.2","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456270}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","requestId":"9990.2","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":141,"connectionReused":true,"encodedDataLength":588,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","access-control-allow-methods":"HEAD, GET","access-control-allow-origin":"*","access-control-max-age":"3000","age":"10964949","cache-control":"max-age=31536000","content-length":"45768","content-type":"binary/octet-stream","date":"Mon, 13 May 2024 06:41:48 GMT","etag":"\\"f2199f841165c4ddbafcf177da3ef974\\"","last-modified":"Thu, 09 May 2024 18:28:30 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Origin,Access-Control-Request-Headers,Access-Control-Request-Method","via":"1.1 19bcf0769b1328ef147a6af36ae38b82.cloudfront.net (CloudFront)","x-amz-cf-id":"gwff2WSN7GG1qU8avfvY6ptHaGNymVvCwdoLZnLX6g7XEY0v0TwybA==","x-amz-cf-pop":"LAX54-P2","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"dkRm0Wve.r.WDBDln90vy9jv3Zt.YaAn","x-cache":"Hit from cloudfront"},"mimeType":"binary/octet-stream","protocol":"h2","remoteIPAddress":"3.168.132.100","remotePort":443,"responseTime":1.726547456270005e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":118.763,"receiveHeadersStart":118.549,"requestTime":1924.951708,"sendEnd":91.54,"sendStart":91.28,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://static-assets.bamgrid.com/fonts/inspire/Inspire-Regular.f2199f841165c4ddbafcf177da3ef974.woff2"},"timestamp":1925.071661,"type":"Font"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456272}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":45768,"encodedDataLength":45822,"requestId":"9990.2","timestamp":1925.072737}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456273}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":46410,"requestId":"9990.2","timestamp":1925.072694}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456273}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.028728},"headers":{":authority":"prod-ripcut-delivery.disney-plus.net",":method":"GET",":path":"/v1/variant/disney/BD389E7A5EF75EB8CFDAB05C134C97232D6F8C097D0C91C3518096BB56463910/scale?width=768&aspectRatio=1.78&format=webp",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"u=2, i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.24","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456295}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1924.961117},"headers":{":authority":"prod-ripcut-delivery.disney-plus.net",":method":"GET",":path":"/v1/variant/disney/5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1/scale?width=768&aspectRatio=1.78&format=webp",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"u=2, i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.23","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456295}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"access-control-expose-headers":"X-BAMTECH-ERROR, X-BAMTECH-TRANSACTION-ID","cache-control":"max-age=2592000","content-length":"44056","content-type":"image/webp","date":"Tue, 17 Sep 2024 04:30:56 GMT","etag":"\\"55b7ae8c95f3b251a26fe44ffb1b5c17\\"","if-modified-since":"Sun, 25 Aug 2024 13:01:11 GMT","lastmodified":"Sun, 25 Aug 2024 13:01:11 GMT","referrer-policy":"origin-when-cross-origin, strict-origin-when-cross-origin","via":"1.1 2c1ef6b20d81714646371fcbdee020c6.cloudfront.net (CloudFront)","x-amz-cf-id":"CowYsfqK9aGt-I7ZUKZ2pEw017rwseoFUIRoPfJJOPVkDsjsVGByAg==","x-amz-cf-pop":"LAX54-P6","x-bamtech-transaction-id":"a6Zmx70cRM0sycgG4ZjG53wE","x-cache":"Miss from cloudfront","x-content-type-options":"nosniff","x-frame-options":"DENY","x-permitted-cross-domain-policies":"master-only","x-xss-protection":"1; mode=block"},"requestId":"9990.24","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456385}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","requestId":"9990.24","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":159,"connectionReused":false,"encodedDataLength":585,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"access-control-expose-headers":"X-BAMTECH-ERROR, X-BAMTECH-TRANSACTION-ID","cache-control":"max-age=2592000","content-length":"44056","content-type":"image/webp","date":"Tue, 17 Sep 2024 04:30:56 GMT","etag":"\\"55b7ae8c95f3b251a26fe44ffb1b5c17\\"","if-modified-since":"Sun, 25 Aug 2024 13:01:11 GMT","lastmodified":"Sun, 25 Aug 2024 13:01:11 GMT","referrer-policy":"origin-when-cross-origin, strict-origin-when-cross-origin","via":"1.1 2c1ef6b20d81714646371fcbdee020c6.cloudfront.net (CloudFront)","x-amz-cf-id":"CowYsfqK9aGt-I7ZUKZ2pEw017rwseoFUIRoPfJJOPVkDsjsVGByAg==","x-amz-cf-pop":"LAX54-P6","x-bamtech-transaction-id":"a6Zmx70cRM0sycgG4ZjG53wE","x-cache":"Miss from cloudfront","x-content-type-options":"nosniff","x-frame-options":"DENY","x-permitted-cross-domain-policies":"master-only","x-xss-protection":"1; mode=block"},"mimeType":"image/webp","protocol":"h2","remoteIPAddress":"13.249.126.15","remotePort":443,"responseTime":1.726547456384577e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":65.7,"connectStart":34.716,"dnsEnd":34.533,"dnsStart":0,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":156.321,"receiveHeadersStart":156.119,"requestTime":1925.028728,"sendEnd":66.409,"sendStart":65.945,"sslEnd":65.693,"sslStart":46.18,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/BD389E7A5EF75EB8CFDAB05C134C97232D6F8C097D0C91C3518096BB56463910/scale?width=768&aspectRatio=1.78&format=webp"},"timestamp":1925.188313,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456389}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":15781,"encodedDataLength":0,"requestId":"9990.24","timestamp":1925.188377}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456389}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":28275,"encodedDataLength":44119,"requestId":"9990.24","timestamp":1925.194095}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456394}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"access-control-expose-headers":"X-BAMTECH-ERROR, X-BAMTECH-TRANSACTION-ID","cache-control":"max-age=2592000","content-length":"41150","content-type":"image/webp","date":"Tue, 17 Sep 2024 04:30:56 GMT","etag":"\\"e00617fe39469fb939d1a3d47a7c9397\\"","if-modified-since":"Wed, 31 Jan 2024 16:32:31 GMT","lastmodified":"Wed, 31 Jan 2024 16:32:31 GMT","referrer-policy":"origin-when-cross-origin, strict-origin-when-cross-origin","via":"1.1 2c1ef6b20d81714646371fcbdee020c6.cloudfront.net (CloudFront)","x-amz-cf-id":"YzDfFX2GOS0bdhzev02MkXMqEJE_MT-qIbRZSfahnlTpweEiB3UR2g==","x-amz-cf-pop":"LAX54-P6","x-bamtech-transaction-id":"ClfRVSuZlQBubBk7UL8WHQ0G","x-cache":"Miss from cloudfront","x-content-type-options":"nosniff","x-frame-options":"DENY","x-permitted-cross-domain-policies":"master-only","x-xss-protection":"1; mode=block"},"requestId":"9990.23","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456394}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":44704,"requestId":"9990.24","timestamp":1925.193655}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456395}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.195612},"headers":{":authority":"prod-ripcut-delivery.disney-plus.net",":method":"GET",":path":"/v1/variant/disney/73EE9910650A52DE775F7E676C539DC8BAC63C4AAF152742A7E5EF1C69429644/scale?width=200&format=webp",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"u=2, i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.25","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456396}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","requestId":"9990.23","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":159,"connectionReused":true,"encodedDataLength":586,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"access-control-expose-headers":"X-BAMTECH-ERROR, X-BAMTECH-TRANSACTION-ID","cache-control":"max-age=2592000","content-length":"41150","content-type":"image/webp","date":"Tue, 17 Sep 2024 04:30:56 GMT","etag":"\\"e00617fe39469fb939d1a3d47a7c9397\\"","if-modified-since":"Wed, 31 Jan 2024 16:32:31 GMT","lastmodified":"Wed, 31 Jan 2024 16:32:31 GMT","referrer-policy":"origin-when-cross-origin, strict-origin-when-cross-origin","via":"1.1 2c1ef6b20d81714646371fcbdee020c6.cloudfront.net (CloudFront)","x-amz-cf-id":"YzDfFX2GOS0bdhzev02MkXMqEJE_MT-qIbRZSfahnlTpweEiB3UR2g==","x-amz-cf-pop":"LAX54-P6","x-bamtech-transaction-id":"ClfRVSuZlQBubBk7UL8WHQ0G","x-cache":"Miss from cloudfront","x-content-type-options":"nosniff","x-frame-options":"DENY","x-permitted-cross-domain-policies":"master-only","x-xss-protection":"1; mode=block"},"mimeType":"image/webp","protocol":"h2","remoteIPAddress":"13.249.126.15","remotePort":443,"responseTime":1.726547456393874e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":233.195,"receiveHeadersStart":233.029,"requestTime":1924.961117,"sendEnd":134.023,"sendStart":133.775,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1/scale?width=768&aspectRatio=1.78&format=webp"},"timestamp":1925.197078,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456397}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":6613,"encodedDataLength":0,"requestId":"9990.23","timestamp":1925.197127}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456397}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":34537,"encodedDataLength":41213,"requestId":"9990.23","timestamp":1925.203269}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456403}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":41799,"requestId":"9990.23","timestamp":1925.202749}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456403}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.20398},"headers":{":authority":"prod-ripcut-delivery.disney-plus.net",":method":"GET",":path":"/v1/variant/disney/FAE63AC7AC11C27C949E1856CF188BF09FC20EA52AEA3B65B43C24EEB5F29BFD/scale?width=200&format=webp",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"u=2, i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.26","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456404}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"access-control-expose-headers":"X-BAMTECH-ERROR, X-BAMTECH-TRANSACTION-ID","age":"1190699","cache-control":"max-age=2592000","content-length":"1794","content-type":"image/webp","date":"Tue, 03 Sep 2024 09:45:57 GMT","etag":"\\"ae5748aed4c079840719be81ee1872bc\\"","if-modified-since":"Thu, 25 Apr 2024 09:17:03 GMT","lastmodified":"Thu, 25 Apr 2024 09:17:03 GMT","referrer-policy":"origin-when-cross-origin, strict-origin-when-cross-origin","via":"1.1 2c1ef6b20d81714646371fcbdee020c6.cloudfront.net (CloudFront)","x-amz-cf-id":"xhHt4qKjsEj-bPhmPA0YqJ3QB3Oee5I7EIWBw0xoM22EcMepX9H0Yw==","x-amz-cf-pop":"LAX54-P6","x-bamtech-transaction-id":"39iAhdSO6udmlrHAXkGusIFt","x-cache":"Hit from cloudfront","x-content-type-options":"nosniff","x-frame-options":"DENY","x-permitted-cross-domain-policies":"master-only","x-xss-protection":"1; mode=block"},"requestId":"9990.25","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456409}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","requestId":"9990.25","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":159,"connectionReused":true,"encodedDataLength":591,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"access-control-expose-headers":"X-BAMTECH-ERROR, X-BAMTECH-TRANSACTION-ID","age":"1190699","cache-control":"max-age=2592000","content-length":"1794","content-type":"image/webp","date":"Tue, 03 Sep 2024 09:45:57 GMT","etag":"\\"ae5748aed4c079840719be81ee1872bc\\"","if-modified-since":"Thu, 25 Apr 2024 09:17:03 GMT","lastmodified":"Thu, 25 Apr 2024 09:17:03 GMT","referrer-policy":"origin-when-cross-origin, strict-origin-when-cross-origin","via":"1.1 2c1ef6b20d81714646371fcbdee020c6.cloudfront.net (CloudFront)","x-amz-cf-id":"xhHt4qKjsEj-bPhmPA0YqJ3QB3Oee5I7EIWBw0xoM22EcMepX9H0Yw==","x-amz-cf-pop":"LAX54-P6","x-bamtech-transaction-id":"39iAhdSO6udmlrHAXkGusIFt","x-cache":"Hit from cloudfront","x-content-type-options":"nosniff","x-frame-options":"DENY","x-permitted-cross-domain-policies":"master-only","x-xss-protection":"1; mode=block"},"mimeType":"image/webp","protocol":"h2","remoteIPAddress":"13.249.126.15","remotePort":443,"responseTime":1.72654745640829e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":13.12,"receiveHeadersStart":12.954,"requestTime":1925.195612,"sendEnd":1.114,"sendStart":0.49,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/73EE9910650A52DE775F7E676C539DC8BAC63C4AAF152742A7E5EF1C69429644/scale?width=200&format=webp"},"timestamp":1925.210173,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456411}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":1794,"encodedDataLength":0,"requestId":"9990.25","timestamp":1925.210229}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456411}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":2403,"requestId":"9990.25","timestamp":1925.209578}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456411}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.211212},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/webpack-7eb13b5b99357ccb.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.8","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456411}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"access-control-expose-headers":"X-BAMTECH-ERROR, X-BAMTECH-TRANSACTION-ID","age":"1416153","cache-control":"max-age=2592000","content-length":"2006","content-type":"image/webp","date":"Sat, 31 Aug 2024 19:08:23 GMT","etag":"\\"6ca8857ef8eb0ee4e4e032f4f136e51d\\"","if-modified-since":"Wed, 17 Jul 2024 13:18:47 GMT","lastmodified":"Wed, 17 Jul 2024 13:18:47 GMT","referrer-policy":"origin-when-cross-origin, strict-origin-when-cross-origin","via":"1.1 2c1ef6b20d81714646371fcbdee020c6.cloudfront.net (CloudFront)","x-amz-cf-id":"77DKF_-Z8KFnH8T7lqykWMe7PW78-Ma7KdDz7_1ybhW0Cb7nH9RDEQ==","x-amz-cf-pop":"LAX54-P6","x-bamtech-transaction-id":"4X64VQU47gSa5Cyw4RoxXDab","x-cache":"Hit from cloudfront","x-content-type-options":"nosniff","x-frame-options":"DENY","x-permitted-cross-domain-policies":"master-only","x-xss-protection":"1; mode=block"},"requestId":"9990.26","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456415}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","requestId":"9990.26","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":159,"connectionReused":true,"encodedDataLength":592,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"access-control-expose-headers":"X-BAMTECH-ERROR, X-BAMTECH-TRANSACTION-ID","age":"1416153","cache-control":"max-age=2592000","content-length":"2006","content-type":"image/webp","date":"Sat, 31 Aug 2024 19:08:23 GMT","etag":"\\"6ca8857ef8eb0ee4e4e032f4f136e51d\\"","if-modified-since":"Wed, 17 Jul 2024 13:18:47 GMT","lastmodified":"Wed, 17 Jul 2024 13:18:47 GMT","referrer-policy":"origin-when-cross-origin, strict-origin-when-cross-origin","via":"1.1 2c1ef6b20d81714646371fcbdee020c6.cloudfront.net (CloudFront)","x-amz-cf-id":"77DKF_-Z8KFnH8T7lqykWMe7PW78-Ma7KdDz7_1ybhW0Cb7nH9RDEQ==","x-amz-cf-pop":"LAX54-P6","x-bamtech-transaction-id":"4X64VQU47gSa5Cyw4RoxXDab","x-cache":"Hit from cloudfront","x-content-type-options":"nosniff","x-frame-options":"DENY","x-permitted-cross-domain-policies":"master-only","x-xss-protection":"1; mode=block"},"mimeType":"image/webp","protocol":"h2","remoteIPAddress":"13.249.126.15","remotePort":443,"responseTime":1.726547456414506e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":10.983,"receiveHeadersStart":10.791,"requestTime":1925.20398,"sendEnd":0.818,"sendStart":0.506,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/FAE63AC7AC11C27C949E1856CF188BF09FC20EA52AEA3B65B43C24EEB5F29BFD/scale?width=200&format=webp"},"timestamp":1925.216354,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456417}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":2006,"encodedDataLength":0,"requestId":"9990.26","timestamp":1925.216419}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456417}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":2607,"requestId":"9990.26","timestamp":1925.215913}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456417}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.217219},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/framework-7ca4c7590a188064.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.9","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456417}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"45330","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:26 GMT","etag":"W/\\"b225fb31e929c65d19756b7fa59db176\\"","last-modified":"Mon, 16 Sep 2024 15:42:54 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"Ekq0g8OA7k8aOgtIYW04cv_pqIYTcBsNRi3Louk1gaIVFTMEsFDinQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"feTJ5FLM6dR6u_XXNMjZfYrDElGHx_li","x-cache":"Hit from cloudfront"},"requestId":"9990.8","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456422}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","requestId":"9990.8","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":469,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"45330","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:26 GMT","etag":"W/\\"b225fb31e929c65d19756b7fa59db176\\"","last-modified":"Mon, 16 Sep 2024 15:42:54 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"Ekq0g8OA7k8aOgtIYW04cv_pqIYTcBsNRi3Louk1gaIVFTMEsFDinQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"feTJ5FLM6dR6u_XXNMjZfYrDElGHx_li","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456421154e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":10.373,"receiveHeadersStart":10.218,"requestTime":1925.211212,"sendEnd":0.631,"sendStart":0.424,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/webpack-7eb13b5b99357ccb.js"},"timestamp":1925.223233,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456426}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":4483,"encodedDataLength":0,"requestId":"9990.8","timestamp":1925.223334}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456426}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.225503},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/main-deda6e05560430d9.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.10","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456427}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":2674,"requestId":"9990.8","timestamp":1925.222661}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456427}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":false,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"Cache-Control":"public, max-age=900, s-maxage=900","Connection":"keep-alive","Content-Encoding":"gzip","Content-Length":"61516","Content-Type":"text/html; charset=utf-8","Date":"Tue, 17 Sep 2024 04:30:56 GMT","Server":"nginx/1.23.2","Vary":"Accept-Encoding","X-Powered-By":"Next.js","X-solo-application":"disneyplus-growth-nsb","disable-redirect":"false","language":"en","pathname":"/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","physical-location":"US","region":"us","url":"/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"headersText":"HTTP/1.1 200 OK\\r\\nContent-Type: text/html; charset=utf-8\\r\\nServer: nginx/1.23.2\\r\\ndisable-redirect: false\\r\\nlanguage: en\\r\\npathname: /series/frieren-beyond-journeys-end/1rlaH8IM0pkQ\\r\\nphysical-location: US\\r\\nregion: us\\r\\nurl: /series/frieren-beyond-journeys-end/1rlaH8IM0pkQ\\r\\nX-Powered-By: Next.js\\r\\nContent-Encoding: gzip\\r\\nX-solo-application: disneyplus-growth-nsb\\r\\nContent-Length: 61516\\r\\nCache-Control: public, max-age=900, s-maxage=900\\r\\nDate: Tue, 17 Sep 2024 04:30:56 GMT\\r\\nConnection: keep-alive\\r\\nVary: Accept-Encoding\\r\\n\\r\\n","requestId":"A217FBA90DB610A58139EB33E6B16822","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456428}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"A217FBA90DB610A58139EB33E6B16822","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"utf-8","connectionId":50,"connectionReused":true,"encodedDataLength":517,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"Cache-Control":"public, max-age=900, s-maxage=900","Connection":"keep-alive","Content-Encoding":"gzip","Content-Length":"61516","Content-Type":"text/html; charset=utf-8","Date":"Tue, 17 Sep 2024 04:30:56 GMT","Server":"nginx/1.23.2","Vary":"Accept-Encoding","X-Powered-By":"Next.js","X-solo-application":"disneyplus-growth-nsb","disable-redirect":"false","language":"en","pathname":"/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","physical-location":"US","region":"us","url":"/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"mimeType":"text/html","protocol":"http/1.1","remoteIPAddress":"23.44.150.44","remotePort":443,"responseTime":1.72654745642777e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_256_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disneyplus.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"304502203DA0ABCDDCF9D90E7EBFB94AEF448502C0DEA7BACC8349DB8A9DF6C5F750E1F3022100828F8E1E047B68CEEFF14D16E14C6CA511694F6416E6F22E0406826D48C1640C","status":"Verified","timestamp":1.706023785126e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100F551968BA749E63D16F0664812317C81D0AC9A23E5B39CBE00D40D30D37CA26F0221009F8FBC335F475EB6DE40D9DBCA060451E85E69D6630CED6DBADDE9C7059FB587","status":"Verified","timestamp":1.706023785204e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"304402207333FD209CD40F2B584EA279D545F2E5591EA3549DB9631FCBA7C8738C260B97022069EBF67DE6B3E71127D290A8C8D95EFFAE332E0856CFE996811CA8B22356D97A","status":"Verified","timestamp":1.706023785094e+12}],"subjectName":"*.disneyplus.com","validFrom":1705968000,"validTo":1737590399},"securityState":"secure","status":200,"statusText":"OK","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":225.339,"receiveHeadersStart":225.205,"requestTime":1925.002876,"sendEnd":0.67,"sendStart":0.553,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"timestamp":1925.229976,"type":"Document"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456430}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"176412","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Sun, 15 Sep 2024 03:30:46 GMT","etag":"W/\\"9f8fe76f2e221f2a66a78c4188396d41\\"","last-modified":"Sat, 07 Sep 2024 06:49:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"F9kSlbim_uSg6Xxjbx3dCsSdLuKp4r5cm9upuzNn7QXhWRdp-iQMvQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"_kaTrb9WC2d3pyDnVlVSmE.13ANbCZjw","x-cache":"Hit from cloudfront"},"requestId":"9990.9","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456435}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"8D7973F50CAAE99C42016BF52D8A5C91","requestId":"9990.9","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":470,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"176412","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Sun, 15 Sep 2024 03:30:46 GMT","etag":"W/\\"9f8fe76f2e221f2a66a78c4188396d41\\"","last-modified":"Sat, 07 Sep 2024 06:49:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"F9kSlbim_uSg6Xxjbx3dCsSdLuKp4r5cm9upuzNn7QXhWRdp-iQMvQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"_kaTrb9WC2d3pyDnVlVSmE.13ANbCZjw","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456428846e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":12.038,"receiveHeadersStart":11.898,"requestTime":1925.217219,"sendEnd":0.682,"sendStart":0.514,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/framework-7ca4c7590a188064.js"},"timestamp":1925.231928,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456436}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":44520,"encodedDataLength":0,"requestId":"9990.9","timestamp":1925.232655}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456436}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"550980","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Tue, 10 Sep 2024 19:27:58 GMT","etag":"W/\\"7063788f862f451b086b25ceceeed9f6\\"","last-modified":"Tue, 10 Sep 2024 19:27:01 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"pQ8rNQbI29qePFDFct4XwDp9GA-Dva2KZ51FIboXI425wBm5c4Rrcw==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"mVvRpzh6gn95JLXByCXUnBlCe3F9nzJY","x-cache":"Hit from cloudfront"},"requestId":"9990.10","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456439}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.243493},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/pages/_app-04a807cd96ff1485.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.11","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456444}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.244619},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/689-1704811563a7aad2.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.12","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456446}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.245978},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/646-9fd3676fcc0efa42.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.13","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456454}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.247437},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/292-02db2ad1e62c2a58.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.15","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456455}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.14","timestamp":1925.242735,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456455}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.24837},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/928-a3fb44f500ddd597.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.16","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456456}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.249079},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/440-afce561b152fc100.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.17","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456457}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.250158},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/U6_u41-7WVYTgYdDlkjYi/_ssgManifest.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.20","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456457}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.18","timestamp":1925.24281,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456457}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.25149},"headers":{":authority":"prod-ripcut-delivery.disney-plus.net",":method":"GET",":path":"/v1/variant/disney/14EC756AA7761F4D01AEF0C21A660AD0778F87EF1487F3369CBB2542DD060DC0/scale?width=600&aspectRatio=1.78&format=webp",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.29","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456458}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.10","timestamp":1925.243415,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456459}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.11","timestamp":1925.244787,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456459}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.9","timestamp":1925.24519,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456459}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.19","timestamp":1925.245401,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456459}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.13","timestamp":1925.246896,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456459}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.12","timestamp":1925.247554,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456459}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.15","timestamp":1925.247803,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456459}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.16","timestamp":1925.248075,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456459}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.20","timestamp":1925.248878,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456459}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.17","timestamp":1925.24918,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456459}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.31","timestamp":1925.249198,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456459}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.21","timestamp":1925.249316,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456459}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.29","timestamp":1925.249349,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456459}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.25282},"headers":{":authority":"prod-ripcut-delivery.disney-plus.net",":method":"GET",":path":"/v1/variant/disney/329B3B6A0FF859ACF4DB56481FB31E660E90B503D0A5FE369F268B4F7E426972/scale?width=600&aspectRatio=1.78&format=webp",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.30","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456459}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.30","timestamp":1925.249394,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456461}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameNavigated","params":{"frame":{"adFrameStatus":{"adFrameType":"none"},"crossOriginIsolatedContextType":"NotIsolated","domainAndRegistry":"disneyplus.com","gatedAPIFeatures":[],"id":"3E7284AA00690624BB019FC4430314BC","loaderId":"A217FBA90DB610A58139EB33E6B16822","mimeType":"text/html","secureContextType":"Secure","securityOrigin":"https://www.disneyplus.com","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"type":"Navigation"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456461}
{'level': 'INFO', 'message': '{"message":{"method":"Network.policyUpdated","params":{}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456465}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":596112,"encodedDataLength":0,"requestId":"A217FBA90DB610A58139EB33E6B16822","timestamp":1925.266712}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456494}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":7023,"lineNumber":0,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Origin":"https://www.disneyplus.com","Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"High","isLinkPreload":true,"isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://static-assets.bamgrid.com/fonts/inspire/Inspire-Regular.f2199f841165c4ddbafcf177da3ef974.woff2"},"requestId":"9990.35","timestamp":1925.279915,"type":"Font","wallTime":1726547456.47966}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456494}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":7203,"lineNumber":0,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Origin":"https://www.disneyplus.com","Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"High","isLinkPreload":true,"isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://static-assets.bamgrid.com/fonts/inspire/Inspire-Bold.4ff15ddc93445342649194969715b0b5.woff2"},"requestId":"9990.36","timestamp":1925.283828,"type":"Font","wallTime":1726547456.483569}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456494}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":173,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"VeryHigh","isLinkPreload":true,"isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/css/d7217ef32a15aede.css"},"requestId":"9990.37","timestamp":1925.285404,"type":"Stylesheet","wallTime":1726547456.485685}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456494}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":481,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"VeryHigh","isLinkPreload":true,"isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/css/b503c746db7a0c4d.css"},"requestId":"9990.39","timestamp":1925.288462,"type":"Stylesheet","wallTime":1726547456.488195}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456494}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":987,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/webpack-7eb13b5b99357ccb.js"},"requestId":"9990.41","timestamp":1925.290451,"type":"Script","wallTime":1726547456.490183}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456494}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":1144,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/framework-7ca4c7590a188064.js"},"requestId":"9990.42","timestamp":1925.290639,"type":"Script","wallTime":1726547456.490591}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456495}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":1296,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/main-deda6e05560430d9.js"},"requestId":"9990.43","timestamp":1925.29107,"type":"Script","wallTime":1726547456.490797}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456495}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":1454,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/pages/_app-04a807cd96ff1485.js"},"requestId":"9990.44","timestamp":1925.291204,"type":"Script","wallTime":1726547456.490914}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456495}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":1605,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/689-1704811563a7aad2.js"},"requestId":"9990.45","timestamp":1925.291322,"type":"Script","wallTime":1726547456.491027}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456495}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":1756,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/646-9fd3676fcc0efa42.js"},"requestId":"9990.46","timestamp":1925.291385,"type":"Script","wallTime":1726547456.491086}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456496}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":1907,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/182-74c9963345086f4c.js"},"requestId":"9990.47","timestamp":1925.29144,"type":"Script","wallTime":1726547456.491143}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456496}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":2058,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/292-02db2ad1e62c2a58.js"},"requestId":"9990.48","timestamp":1925.291494,"type":"Script","wallTime":1726547456.491195}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456496}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":2209,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/928-a3fb44f500ddd597.js"},"requestId":"9990.49","timestamp":1925.29155,"type":"Script","wallTime":1726547456.491251}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456496}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":2360,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/440-afce561b152fc100.js"},"requestId":"9990.50","timestamp":1925.291619,"type":"Script","wallTime":1726547456.491329}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456496}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":2549,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/pages/series/%5BprettyTitle%5D/%5Bslug%5D-b604066ab3641502.js"},"requestId":"9990.51","timestamp":1925.291727,"type":"Script","wallTime":1726547456.491476}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456496}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":2709,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/U6_u41-7WVYTgYdDlkjYi/_buildManifest.js"},"requestId":"9990.52","timestamp":1925.291892,"type":"Script","wallTime":1726547456.491603}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456496}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":2867,"lineNumber":267,"type":"parser","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/U6_u41-7WVYTgYdDlkjYi/_ssgManifest.js"},"requestId":"9990.53","timestamp":1925.29203,"type":"Script","wallTime":1726547456.49175}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456496}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":false,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.35","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":0,"connectionReused":false,"encodedDataLength":0,"fromDiskCache":true,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","access-control-allow-methods":"HEAD, GET","access-control-allow-origin":"*","access-control-max-age":"3000","age":"10964949","cache-control":"max-age=31536000","content-length":"45768","content-type":"binary/octet-stream","date":"Mon, 13 May 2024 06:41:48 GMT","etag":"\\"f2199f841165c4ddbafcf177da3ef974\\"","last-modified":"Thu, 09 May 2024 18:28:30 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Origin,Access-Control-Request-Headers,Access-Control-Request-Method","via":"1.1 19bcf0769b1328ef147a6af36ae38b82.cloudfront.net (CloudFront)","x-amz-cf-id":"gwff2WSN7GG1qU8avfvY6ptHaGNymVvCwdoLZnLX6g7XEY0v0TwybA==","x-amz-cf-pop":"LAX54-P2","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"dkRm0Wve.r.WDBDln90vy9jv3Zt.YaAn","x-cache":"Hit from cloudfront"},"mimeType":"binary/octet-stream","protocol":"h2","remoteIPAddress":"3.168.132.100","remotePort":443,"responseTime":1.726547456270005e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"unknown","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":0.527,"receiveHeadersStart":0.437,"requestTime":1925.280495,"sendEnd":0.103,"sendStart":0.103,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://static-assets.bamgrid.com/fonts/inspire/Inspire-Regular.f2199f841165c4ddbafcf177da3ef974.woff2"},"timestamp":1925.295392,"type":"Font"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456501}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":45768,"encodedDataLength":0,"requestId":"9990.35","timestamp":1925.295452}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456501}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":0,"requestId":"9990.35","timestamp":1925.282911}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456501}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":false,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.36","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":0,"connectionReused":false,"encodedDataLength":0,"fromDiskCache":true,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","access-control-allow-methods":"HEAD, GET","access-control-allow-origin":"*","access-control-max-age":"3000","age":"9360815","cache-control":"max-age=31536000","content-length":"47404","content-type":"binary/octet-stream","date":"Fri, 31 May 2024 20:17:22 GMT","etag":"\\"4ff15ddc93445342649194969715b0b5\\"","last-modified":"Tue, 14 May 2024 15:02:51 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Origin,Access-Control-Request-Headers,Access-Control-Request-Method","via":"1.1 19bcf0769b1328ef147a6af36ae38b82.cloudfront.net (CloudFront)","x-amz-cf-id":"-YQoIYE5LXG5_7d4a29oBVNOCAGDZkoLWmbPHhESlP3fFZkh8vhMxw==","x-amz-cf-pop":"LAX54-P2","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"mHgivmJvrFPL1bt8KLmQabrk3A21esyc","x-cache":"Hit from cloudfront"},"mimeType":"binary/octet-stream","protocol":"h2","remoteIPAddress":"3.168.132.100","remotePort":443,"responseTime":1.726547456253331e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"unknown","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":0.48,"receiveHeadersStart":0.261,"requestTime":1925.284323,"sendEnd":0.091,"sendStart":0.091,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://static-assets.bamgrid.com/fonts/inspire/Inspire-Bold.4ff15ddc93445342649194969715b0b5.woff2"},"timestamp":1925.296077,"type":"Font"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456501}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":47404,"encodedDataLength":0,"requestId":"9990.36","timestamp":1925.296117}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456501}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":0,"requestId":"9990.36","timestamp":1925.285516}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456501}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":false,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.37","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":0,"connectionReused":false,"encodedDataLength":0,"fromDiskCache":true,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"521388","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"text/css","date":"Wed, 11 Sep 2024 03:41:09 GMT","etag":"W/\\"91bccef3f66ef49a2c3b4c10f64a4ae1\\"","last-modified":"Wed, 11 Sep 2024 01:08:31 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"0SC7Do3O7v_FZtLLEFvOR4qVjDgnUgaO2S7BXa5kZKOLi709PKtr6Q==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"7v1FKlNNElbUZUeZLFHcLOgB3qrfRqmL","x-cache":"Hit from cloudfront"},"mimeType":"text/css","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456256106e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"unknown","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":0.471,"receiveHeadersStart":0.398,"requestTime":1925.286364,"sendEnd":0.126,"sendStart":0.126,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/css/d7217ef32a15aede.css"},"timestamp":1925.296736,"type":"Stylesheet"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456501}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":59603,"encodedDataLength":0,"requestId":"9990.37","timestamp":1925.296775}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456501}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":0,"requestId":"9990.37","timestamp":1925.287823}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456501}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":false,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.39","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":0,"connectionReused":false,"encodedDataLength":0,"fromDiskCache":true,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"528184","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"text/css","date":"Wed, 11 Sep 2024 07:28:19 GMT","etag":"W/\\"ac4c71354de0b6914046a44ebadfc3eb\\"","last-modified":"Wed, 04 Sep 2024 02:38:48 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"G7n9yuTGmMpjVG4A8CK_RnFz2XbU27iegOzy5XuuvVocU2wEkaN09A==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"i1iMYDX6RR9tECwvwQkOijolVLr_ntV3","x-cache":"Hit from cloudfront"},"mimeType":"text/css","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456257968e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"unknown","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":0.455,"receiveHeadersStart":0.379,"requestTime":1925.288857,"sendEnd":0.116,"sendStart":0.116,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/css/b503c746db7a0c4d.css"},"timestamp":1925.298378,"type":"Stylesheet"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456501}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":14187,"encodedDataLength":0,"requestId":"9990.39","timestamp":1925.298414}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456501}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":0,"requestId":"9990.39","timestamp":1925.290103}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456501}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameScheduledNavigation","params":{"delay":0,"frameId":"3E7284AA00690624BB019FC4430314BC","reason":"scriptInitiated","url":"https://www.disneyplus.com/"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456517}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameRequestedNavigation","params":{"disposition":"currentTab","frameId":"3E7284AA00690624BB019FC4430314BC","reason":"scriptInitiated","url":"https://www.disneyplus.com/"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456517}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameStartedLoading","params":{"frameId":"3E7284AA00690624BB019FC4430314BC"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456520}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"stack":{"callFrames":[{"columnNumber":29,"functionName":"langRegionRedirect","lineNumber":247,"scriptId":"10","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"},{"columnNumber":46,"functionName":"","lineNumber":263,"scriptId":"10","url":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ"}]},"type":"script"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"VeryHigh","isSameSite":true,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://www.disneyplus.com/"},"requestId":"939C9171ED8FE2B6C35C286E1883435F","timestamp":1925.321738,"type":"Document","wallTime":1726547456.521458}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456521}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameClearedScheduledNavigation","params":{"frameId":"3E7284AA00690624BB019FC4430314BC"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456523}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"type":"other"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Medium","isSameSite":true,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://www.disneyplus.com/manifest.json"},"requestId":"9990.56","timestamp":1925.319514,"type":"Manifest","wallTime":1726547456.519262}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456523}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"Allow"},"connectTiming":{"requestTime":1925.322793},"headers":{"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"en-US,en;q=0.9","Connection":"keep-alive","Host":"www.disneyplus.com","Referer":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","Sec-Fetch-Dest":"document","Sec-Fetch-Mode":"navigate","Sec-Fetch-Site":"same-origin","Upgrade-Insecure-Requests":"1","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"requestId":"939C9171ED8FE2B6C35C286E1883435F","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456524}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":62033,"requestId":"A217FBA90DB610A58139EB33E6B16822","timestamp":1925.233389}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456525}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":false,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.41","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":0,"connectionReused":false,"encodedDataLength":0,"fromDiskCache":true,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"45330","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:26 GMT","etag":"W/\\"b225fb31e929c65d19756b7fa59db176\\"","last-modified":"Mon, 16 Sep 2024 15:42:54 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"Ekq0g8OA7k8aOgtIYW04cv_pqIYTcBsNRi3Louk1gaIVFTMEsFDinQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"feTJ5FLM6dR6u_XXNMjZfYrDElGHx_li","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456421154e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"unknown","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":0.704,"receiveHeadersStart":0.632,"requestTime":1925.297706,"sendEnd":0.137,"sendStart":0.137,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/webpack-7eb13b5b99357ccb.js"},"timestamp":1925.325597,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456526}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":4483,"encodedDataLength":0,"requestId":"9990.41","timestamp":1925.325674}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456528}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":false,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.42","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":0,"connectionReused":false,"encodedDataLength":0,"fromDiskCache":true,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"176412","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Sun, 15 Sep 2024 03:30:46 GMT","etag":"W/\\"9f8fe76f2e221f2a66a78c4188396d41\\"","last-modified":"Sat, 07 Sep 2024 06:49:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"F9kSlbim_uSg6Xxjbx3dCsSdLuKp4r5cm9upuzNn7QXhWRdp-iQMvQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"_kaTrb9WC2d3pyDnVlVSmE.13ANbCZjw","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456428846e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"unknown","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":0.776,"receiveHeadersStart":0.711,"requestTime":1925.29895,"sendEnd":0.135,"sendStart":0.135,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/framework-7ca4c7590a188064.js"},"timestamp":1925.326327,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456528}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":141069,"encodedDataLength":0,"requestId":"9990.42","timestamp":1925.326382}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456528}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":0,"requestId":"9990.41","timestamp":1925.29943}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456528}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":0,"requestId":"9990.42","timestamp":1925.30415}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456534}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":false,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.43","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":0,"connectionReused":false,"encodedDataLength":0,"fromDiskCache":true,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"550980","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Tue, 10 Sep 2024 19:27:58 GMT","etag":"W/\\"7063788f862f451b086b25ceceeed9f6\\"","last-modified":"Tue, 10 Sep 2024 19:27:01 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"pQ8rNQbI29qePFDFct4XwDp9GA-Dva2KZ51FIboXI425wBm5c4Rrcw==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"mVvRpzh6gn95JLXByCXUnBlCe3F9nzJY","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456438201e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"unknown","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":0.701,"receiveHeadersStart":0.609,"requestTime":1925.334206,"sendEnd":0.131,"sendStart":0.131,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/main-deda6e05560430d9.js"},"timestamp":1925.336474,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456538}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":112926,"encodedDataLength":0,"requestId":"9990.43","timestamp":1925.336572}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456538}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":9651,"encodedDataLength":0,"requestId":"9990.43","timestamp":1925.344188}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456545}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":0,"requestId":"9990.43","timestamp":1925.336636}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456546}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.344882},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/pages/_app-04a807cd96ff1485.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.44","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456546}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.320106},"headers":{"Accept":"*/*","Accept-Encoding":"gzip, deflate, br, zstd","Accept-Language":"en-US,en;q=0.9","Connection":"keep-alive","Host":"www.disneyplus.com","Referer":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","Sec-Fetch-Dest":"manifest","Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"requestId":"9990.56","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456546}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"45329","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:28 GMT","etag":"W/\\"8cfefecab1f8564801fa38855f65c511\\"","last-modified":"Mon, 16 Sep 2024 15:42:54 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"idlkbz5nh7hNyfUF7AQ6tLIGea5FYrYWVJX5Cz50WOIkT7uiWgqZVg==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"Mqi.IIylvPTTUsGMlyTd5wh49VSUN9Y_","x-cache":"Hit from cloudfront"},"requestId":"9990.44","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456555}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.44","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":470,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"45329","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:28 GMT","etag":"W/\\"8cfefecab1f8564801fa38855f65c511\\"","last-modified":"Mon, 16 Sep 2024 15:42:54 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"idlkbz5nh7hNyfUF7AQ6tLIGea5FYrYWVJX5Cz50WOIkT7uiWgqZVg==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"Mqi.IIylvPTTUsGMlyTd5wh49VSUN9Y_","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456554907e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":10.48,"receiveHeadersStart":10.305,"requestTime":1925.344882,"sendEnd":0.588,"sendStart":0.414,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/pages/_app-04a807cd96ff1485.js"},"timestamp":1925.359606,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456562}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":95594,"encodedDataLength":0,"requestId":"9990.44","timestamp":1925.359819}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456562}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":false,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"Access-Control-Allow-Methods":"HEAD, GET","Access-Control-Allow-Origin":"*","Access-Control-Max-Age":"3000","Cache-Control":"max-age=34","Connection":"keep-alive","Content-Encoding":"gzip","Content-Length":"449","Content-Type":"application/json","Date":"Tue, 17 Sep 2024 04:30:56 GMT","ETag":"W/\\"79399f9bae72975dad01ed3c5fdf111c\\"","Last-Modified":"Thu, 22 Aug 2024 18:55:38 GMT","Server":"AmazonS3","Timing-Allow-Origin":"*","Vary":"Accept-Encoding","X-Amz-Cf-Id":"K0l088iRM3oqi_4RmVr5C-0UnllzbCNyvw9XR0hgJ2ojr2i9xp-uHA==","X-Amz-Cf-Pop":"LAX50-C3","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":".IiqWQGsKEORzPKlyxGhTM.64LsyvIK7"},"headersText":"HTTP/1.1 200 OK\\r\\nContent-Type: application/json\\r\\nAccess-Control-Allow-Origin: *\\r\\nAccess-Control-Allow-Methods: HEAD, GET\\r\\nAccess-Control-Max-Age: 3000\\r\\nx-amz-replication-status: COMPLETED\\r\\nLast-Modified: Thu, 22 Aug 2024 18:55:38 GMT\\r\\nETag: W/\\"79399f9bae72975dad01ed3c5fdf111c\\"\\r\\nx-amz-server-side-encryption: AES256\\r\\nx-amz-version-id: .IiqWQGsKEORzPKlyxGhTM.64LsyvIK7\\r\\nServer: AmazonS3\\r\\nContent-Encoding: gzip\\r\\nX-Amz-Cf-Pop: LAX50-C3\\r\\nX-Amz-Cf-Id: K0l088iRM3oqi_4RmVr5C-0UnllzbCNyvw9XR0hgJ2ojr2i9xp-uHA==\\r\\nTiming-Allow-Origin: *\\r\\nContent-Length: 449\\r\\nCache-Control: max-age=34\\r\\nDate: Tue, 17 Sep 2024 04:30:56 GMT\\r\\nConnection: keep-alive\\r\\nVary: Accept-Encoding\\r\\n\\r\\n","requestId":"9990.56","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456570}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.56","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":275,"connectionReused":false,"encodedDataLength":664,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"Access-Control-Allow-Methods":"HEAD, GET","Access-Control-Allow-Origin":"*","Access-Control-Max-Age":"3000","Cache-Control":"max-age=34","Connection":"keep-alive","Content-Encoding":"gzip","Content-Length":"449","Content-Type":"application/json","Date":"Tue, 17 Sep 2024 04:30:56 GMT","ETag":"W/\\"79399f9bae72975dad01ed3c5fdf111c\\"","Last-Modified":"Thu, 22 Aug 2024 18:55:38 GMT","Server":"AmazonS3","Timing-Allow-Origin":"*","Vary":"Accept-Encoding","X-Amz-Cf-Id":"K0l088iRM3oqi_4RmVr5C-0UnllzbCNyvw9XR0hgJ2ojr2i9xp-uHA==","X-Amz-Cf-Pop":"LAX50-C3","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":".IiqWQGsKEORzPKlyxGhTM.64LsyvIK7"},"mimeType":"application/json","protocol":"http/1.1","remoteIPAddress":"23.44.150.44","remotePort":443,"responseTime":1.726547456569791e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_256_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disneyplus.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"304502203DA0ABCDDCF9D90E7EBFB94AEF448502C0DEA7BACC8349DB8A9DF6C5F750E1F3022100828F8E1E047B68CEEFF14D16E14C6CA511694F6416E6F22E0406826D48C1640C","status":"Verified","timestamp":1.706023785126e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100F551968BA749E63D16F0664812317C81D0AC9A23E5B39CBE00D40D30D37CA26F0221009F8FBC335F475EB6DE40D9DBCA060451E85E69D6630CED6DBADDE9C7059FB587","status":"Verified","timestamp":1.706023785204e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"304402207333FD209CD40F2B584EA279D545F2E5591EA3549DB9631FCBA7C8738C260B97022069EBF67DE6B3E71127D290A8C8D95EFFAE332E0856CFE996811CA8B22356D97A","status":"Verified","timestamp":1.706023785094e+12}],"subjectName":"*.disneyplus.com","validFrom":1705968000,"validTo":1737590399},"securityState":"secure","status":200,"statusText":"OK","timing":{"connectEnd":26.215,"connectStart":0.4,"dnsEnd":0.4,"dnsStart":0.388,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":50.139,"receiveHeadersStart":49.996,"requestTime":1925.320106,"sendEnd":26.412,"sendStart":26.315,"sslEnd":26.207,"sslStart":9.031,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://www.disneyplus.com/manifest.json"},"timestamp":1925.371304,"type":"Manifest"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456576}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":1139,"encodedDataLength":449,"requestId":"9990.56","timestamp":1925.372775}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456576}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":1113,"requestId":"9990.56","timestamp":1925.371772}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456576}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.373819},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/689-1704811563a7aad2.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.45","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456577}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"type":"other"},"loaderId":"A217FBA90DB610A58139EB33E6B16822","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"High","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://static-assets.bamgrid.com/product/disneyplus/favicons/msftpwa-192x192-aurora.97f08a1eb58995c81687d0cf3f953796.png"},"requestId":"9990.57","timestamp":1925.379532,"type":"Other","wallTime":1726547456.579267}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456581}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"521388","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Wed, 11 Sep 2024 03:41:09 GMT","etag":"W/\\"28c6c7f006aa2a1386dcdf87054e83db\\"","last-modified":"Wed, 11 Sep 2024 01:08:30 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"UEzDtjMrYjsOxdD6Rqsz88drJooKZGWeY1Cf9XmSfdiLf7L-A27PhQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"9YZXuUVT8wiWLD_n5p2VAuBYPpETErQE","x-cache":"Hit from cloudfront"},"requestId":"9990.45","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456588}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":382431,"encodedDataLength":657875,"requestId":"9990.44","timestamp":1925.3878}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456589}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.382063},"headers":{":authority":"static-assets.bamgrid.com",":method":"GET",":path":"/product/disneyplus/favicons/msftpwa-192x192-aurora.97f08a1eb58995c81687d0cf3f953796.png",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"u=1, i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.57","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456593}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.45","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":471,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"521388","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Wed, 11 Sep 2024 03:41:09 GMT","etag":"W/\\"28c6c7f006aa2a1386dcdf87054e83db\\"","last-modified":"Wed, 11 Sep 2024 01:08:30 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"UEzDtjMrYjsOxdD6Rqsz88drJooKZGWeY1Cf9XmSfdiLf7L-A27PhQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"9YZXuUVT8wiWLD_n5p2VAuBYPpETErQE","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456587227e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":13.857,"receiveHeadersStart":13.677,"requestTime":1925.373819,"sendEnd":2.575,"sendStart":1.055,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/689-1704811563a7aad2.js"},"timestamp":1925.390317,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456595}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":64780,"encodedDataLength":0,"requestId":"9990.45","timestamp":1925.390404}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456595}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":18464,"requestId":"9990.45","timestamp":1925.389439}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456599}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","age":"62","cache-control":"max-age=300","content-length":"46114","content-type":"image/png","date":"Tue, 17 Sep 2024 04:29:55 GMT","etag":"\\"97f08a1eb58995c81687d0cf3f953796\\"","last-modified":"Wed, 28 Aug 2024 21:28:06 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 db760bd4935f16e1b5c20ab5690be478.cloudfront.net (CloudFront)","x-amz-cf-id":"afTNPop0cqNwm0RYZniKoSDaMmZ7ey_klI7bM052PEVRjHfepq4AFA==","x-amz-cf-pop":"LAX54-P2","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"C_wyL.fslbZiYCtHWIt3D7ob5c0.C3Mz","x-cache":"Hit from cloudfront"},"requestId":"9990.57","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456602}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.57","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":243,"connectionReused":false,"encodedDataLength":460,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","age":"62","cache-control":"max-age=300","content-length":"46114","content-type":"image/png","date":"Tue, 17 Sep 2024 04:29:55 GMT","etag":"\\"97f08a1eb58995c81687d0cf3f953796\\"","last-modified":"Wed, 28 Aug 2024 21:28:06 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 db760bd4935f16e1b5c20ab5690be478.cloudfront.net (CloudFront)","x-amz-cf-id":"afTNPop0cqNwm0RYZniKoSDaMmZ7ey_klI7bM052PEVRjHfepq4AFA==","x-amz-cf-pop":"LAX54-P2","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"C_wyL.fslbZiYCtHWIt3D7ob5c0.C3Mz","x-cache":"Hit from cloudfront"},"mimeType":"image/png","protocol":"h2","remoteIPAddress":"3.168.132.100","remotePort":443,"responseTime":1.726547456601479e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":20.07,"receiveHeadersStart":19.684,"requestTime":1925.382063,"sendEnd":10.656,"sendStart":8.056,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://static-assets.bamgrid.com/product/disneyplus/favicons/msftpwa-192x192-aurora.97f08a1eb58995c81687d0cf3f953796.png"},"timestamp":1925.405458,"type":"Other"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456606}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":15906,"encodedDataLength":0,"requestId":"9990.57","timestamp":1925.405579}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456606}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.41304},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/646-9fd3676fcc0efa42.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.46","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456613}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":30208,"encodedDataLength":46168,"requestId":"9990.57","timestamp":1925.411354}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456620}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":46628,"requestId":"9990.57","timestamp":1925.410845}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456620}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"176411","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Sun, 15 Sep 2024 03:30:46 GMT","etag":"W/\\"c04aa023b1280051490140ecf9876d6b\\"","last-modified":"Sat, 07 Sep 2024 06:49:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"j5ij1WUf-lSLCtk7VaKWaSaq65f2GIG60fNzfM4UJFP3lSdkb3ct3w==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"UixKbGS2nkKmiKsameLWOi482KjZdte5","x-cache":"Hit from cloudfront"},"requestId":"9990.46","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456626}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.46","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":468,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"176411","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Sun, 15 Sep 2024 03:30:46 GMT","etag":"W/\\"c04aa023b1280051490140ecf9876d6b\\"","last-modified":"Sat, 07 Sep 2024 06:49:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"j5ij1WUf-lSLCtk7VaKWaSaq65f2GIG60fNzfM4UJFP3lSdkb3ct3w==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"UixKbGS2nkKmiKsameLWOi482KjZdte5","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456623174e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":10.613,"receiveHeadersStart":10.285,"requestTime":1925.41304,"sendEnd":0.729,"sendStart":0.525,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/646-9fd3676fcc0efa42.js"},"timestamp":1925.428342,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456631}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":11679,"encodedDataLength":0,"requestId":"9990.46","timestamp":1925.428429}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456631}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.431806},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/182-74c9963345086f4c.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.47","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456632}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":4751,"requestId":"9990.46","timestamp":1925.425385}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456632}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"45329","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:27 GMT","etag":"W/\\"ff337b8a46c3554199e86f727553d902\\"","last-modified":"Mon, 16 Sep 2024 15:31:04 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"E4hChk_Y_pEZWihKXob8N29znFCg7GJdNzx4KWZHx0HwiG3fn_mLjQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"N05LXGnVWpQu_DUghA9.8ZpxUgLT6C85","x-cache":"Hit from cloudfront"},"requestId":"9990.47","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456643}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.47","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":471,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"45329","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:27 GMT","etag":"W/\\"ff337b8a46c3554199e86f727553d902\\"","last-modified":"Mon, 16 Sep 2024 15:31:04 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"E4hChk_Y_pEZWihKXob8N29znFCg7GJdNzx4KWZHx0HwiG3fn_mLjQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"N05LXGnVWpQu_DUghA9.8ZpxUgLT6C85","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456642315e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":10.966,"receiveHeadersStart":10.782,"requestTime":1925.431806,"sendEnd":0.807,"sendStart":0.629,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/182-74c9963345086f4c.js"},"timestamp":1925.444595,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456647}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":64451,"encodedDataLength":0,"requestId":"9990.47","timestamp":1925.444687}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456647}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":13732,"requestId":"9990.47","timestamp":1925.443925}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456652}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.451736},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/292-02db2ad1e62c2a58.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.48","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456652}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"422858","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Thu, 12 Sep 2024 07:03:19 GMT","etag":"W/\\"6333d84de208462e72b8757adad3c48c\\"","last-modified":"Thu, 12 Sep 2024 05:14:32 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"eTy8Qw0VBKH0R1lAB1ai3Ohzad70nljXh2pAbMkV_xWjAhOXFO35og==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"WqPV62Z4.qmWuLEHcNnBp.xBQGyGRUPe","x-cache":"Hit from cloudfront"},"requestId":"9990.48","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456665}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":1619127,"encodedDataLength":0,"requestId":"9990.44","timestamp":1925.462898}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456665}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.48","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":470,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"422858","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Thu, 12 Sep 2024 07:03:19 GMT","etag":"W/\\"6333d84de208462e72b8757adad3c48c\\"","last-modified":"Thu, 12 Sep 2024 05:14:32 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"eTy8Qw0VBKH0R1lAB1ai3Ohzad70nljXh2pAbMkV_xWjAhOXFO35og==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"WqPV62Z4.qmWuLEHcNnBp.xBQGyGRUPe","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.72654745666284e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":11.565,"receiveHeadersStart":11.366,"requestTime":1925.451736,"sendEnd":0.591,"sendStart":0.41,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/292-02db2ad1e62c2a58.js"},"timestamp":1925.466301,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456670}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":54425,"encodedDataLength":0,"requestId":"9990.48","timestamp":1925.466392}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456670}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":13700,"requestId":"9990.48","timestamp":1925.464375}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456671}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.471836},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/928-a3fb44f500ddd597.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.49","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456673}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"521388","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Wed, 11 Sep 2024 03:41:09 GMT","etag":"W/\\"59f1c40558f8d9c3fb440f1c21b1192c\\"","last-modified":"Wed, 11 Sep 2024 01:08:30 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"HRF6ChlG5WfCp_-REvS905NFPa9ux2SkrZzlNY2_-L8AjtJEoBR3Zw==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"_a6CGaRbOeTRxNWxqxTKhVab4AVe0eXL","x-cache":"Hit from cloudfront"},"requestId":"9990.49","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456685}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.49","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":471,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"521388","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Wed, 11 Sep 2024 03:41:09 GMT","etag":"W/\\"59f1c40558f8d9c3fb440f1c21b1192c\\"","last-modified":"Wed, 11 Sep 2024 01:08:30 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"HRF6ChlG5WfCp_-REvS905NFPa9ux2SkrZzlNY2_-L8AjtJEoBR3Zw==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"_a6CGaRbOeTRxNWxqxTKhVab4AVe0eXL","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.72654745668273e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":11.38,"receiveHeadersStart":11.012,"requestTime":1925.471836,"sendEnd":1.017,"sendStart":0.701,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/928-a3fb44f500ddd597.js"},"timestamp":1925.48509,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456687}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":5735,"encodedDataLength":0,"requestId":"9990.49","timestamp":1925.48519}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456687}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":2907,"requestId":"9990.49","timestamp":1925.484373}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456688}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.488204},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/440-afce561b152fc100.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.50","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456688}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"45328","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:29 GMT","etag":"W/\\"de318dc6dae68e64729c9c3495b77603\\"","last-modified":"Mon, 16 Sep 2024 15:31:04 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"NtMIUmuqIhh7SOxWyGSGEo3IlFQfw36lMafNlf8BYN6Mua_kbObM2g==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"1KNNEiBbbTi7NBmHOw6vlMKvVodG_yfy","x-cache":"Hit from cloudfront"},"requestId":"9990.50","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456700}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.50","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":469,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"45328","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:29 GMT","etag":"W/\\"de318dc6dae68e64729c9c3495b77603\\"","last-modified":"Mon, 16 Sep 2024 15:31:04 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"NtMIUmuqIhh7SOxWyGSGEo3IlFQfw36lMafNlf8BYN6Mua_kbObM2g==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"1KNNEiBbbTi7NBmHOw6vlMKvVodG_yfy","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456698839e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":11.105,"receiveHeadersStart":10.906,"requestTime":1925.488204,"sendEnd":0.524,"sendStart":0.35,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/440-afce561b152fc100.js"},"timestamp":1925.504401,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456707}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":21136,"encodedDataLength":0,"requestId":"9990.50","timestamp":1925.504504}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456707}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":7596,"requestId":"9990.50","timestamp":1925.500869}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456707}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.506761},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/pages/series/%5BprettyTitle%5D/%5Bslug%5D-b604066ab3641502.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.51","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456708}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"45328","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:29 GMT","etag":"W/\\"1f051ffe4cfc84a30fdeae1018c92a34\\"","last-modified":"Mon, 16 Sep 2024 15:31:05 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"YlykG6SvBBEBQECpbOCGVIwwCAJcyIImaZOXyJfNdxN-s0BxDKwYbg==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"SILQzHXN2RCcqWse2Pd5Q37mF5r8Mb2M","x-cache":"Hit from cloudfront"},"requestId":"9990.51","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456719}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.51","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":470,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"45328","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:29 GMT","etag":"W/\\"1f051ffe4cfc84a30fdeae1018c92a34\\"","last-modified":"Mon, 16 Sep 2024 15:31:05 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"YlykG6SvBBEBQECpbOCGVIwwCAJcyIImaZOXyJfNdxN-s0BxDKwYbg==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"SILQzHXN2RCcqWse2Pd5Q37mF5r8Mb2M","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456717863e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":11.531,"receiveHeadersStart":11.376,"requestTime":1925.506761,"sendEnd":1.501,"sendStart":1.324,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/pages/series/%5BprettyTitle%5D/%5Bslug%5D-b604066ab3641502.js"},"timestamp":1925.520168,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456721}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":4345,"encodedDataLength":0,"requestId":"9990.51","timestamp":1925.520267}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456721}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.521447},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/U6_u41-7WVYTgYdDlkjYi/_buildManifest.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.52","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456722}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":1968,"requestId":"9990.51","timestamp":1925.519055}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456723}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"45330","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:27 GMT","etag":"W/\\"8ca733dcb6282292371945c9e1b59a5f\\"","last-modified":"Sat, 14 Sep 2024 00:19:41 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"1LKSVbRnrhTzbb5vH0MpfZ8-LPZr9aVrPqYMmtVjKJFMWT_-2it5gQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"e4G7888iULNtvYA90tZpNxo4aLdlOOJL","x-cache":"Hit from cloudfront"},"requestId":"9990.52","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456733}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.52","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":468,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"45330","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:27 GMT","etag":"W/\\"8ca733dcb6282292371945c9e1b59a5f\\"","last-modified":"Sat, 14 Sep 2024 00:19:41 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"1LKSVbRnrhTzbb5vH0MpfZ8-LPZr9aVrPqYMmtVjKJFMWT_-2it5gQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"e4G7888iULNtvYA90tZpNxo4aLdlOOJL","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456731624e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":10.669,"receiveHeadersStart":10.357,"requestTime":1925.521447,"sendEnd":0.714,"sendStart":0.507,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/U6_u41-7WVYTgYdDlkjYi/_buildManifest.js"},"timestamp":1925.534206,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456735}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":1949,"encodedDataLength":0,"requestId":"9990.52","timestamp":1925.534287}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456735}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":1217,"requestId":"9990.52","timestamp":1925.532983}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456738}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.537802},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/marketing-unified/_next/static/U6_u41-7WVYTgYdDlkjYi/_ssgManifest.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.53","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456738}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":859197,"encodedDataLength":0,"requestId":"9990.44","timestamp":1925.545368}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456746}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","age":"45331","cache-control":"max-age=604800","content-length":"77","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:26 GMT","etag":"\\"b6652df95db52feb4daf4eca35380933\\"","last-modified":"Sat, 14 Sep 2024 00:19:41 GMT","server":"AmazonS3","timing-allow-origin":"*","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"UMOl-bmN237VpB6SknmBAudgp0a57pL1J_CUCIdXUJoZAqAwT_KQJg==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"T3ZNvdDuyBXO_FdKNIfWj7STAgODxuoo","x-cache":"Hit from cloudfront"},"requestId":"9990.53","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456752}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"A217FBA90DB610A58139EB33E6B16822","requestId":"9990.53","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":454,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","age":"45331","cache-control":"max-age=604800","content-length":"77","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:55:26 GMT","etag":"\\"b6652df95db52feb4daf4eca35380933\\"","last-modified":"Sat, 14 Sep 2024 00:19:41 GMT","server":"AmazonS3","timing-allow-origin":"*","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"UMOl-bmN237VpB6SknmBAudgp0a57pL1J_CUCIdXUJoZAqAwT_KQJg==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"T3ZNvdDuyBXO_FdKNIfWj7STAgODxuoo","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547456750142e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":12.767,"receiveHeadersStart":12.619,"requestTime":1925.537802,"sendEnd":0.643,"sendStart":0.442,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/U6_u41-7WVYTgYdDlkjYi/_ssgManifest.js"},"timestamp":1925.551917,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456753}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":77,"encodedDataLength":0,"requestId":"9990.53","timestamp":1925.552022}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456753}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":540,"requestId":"9990.53","timestamp":1925.551407}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456753}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":658345,"requestId":"9990.44","timestamp":1925.409316}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456764}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"939C9171ED8FE2B6C35C286E1883435F","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"utf-8","connectionId":50,"connectionReused":true,"encodedDataLength":1161,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"Cache-Control":"max-age=0, no-cache, no-store","Connection":"keep-alive","Content-Encoding":"gzip","Content-Length":"77593","Content-Security-Policy":"frame-ancestors \'self\';img-src \'self\' https://* data:;script-src \'self\' \'unsafe-inline\' \'unsafe-eval\' https://* *.disneyplus.com:*;worker-src \'self\' blob:;manifest-src \'self\' *.disneyplus.com;base-uri \'self\';font-src \'self\' https: data:;form-action \'self\';object-src \'none\';script-src-attr \'none\';style-src \'self\' https: \'unsafe-inline\';upgrade-insecure-requests","Content-Type":"text/html; charset=utf-8","Date":"Tue, 17 Sep 2024 04:30:56 GMT","Expires":"Tue, 17 Sep 2024 04:30:56 GMT","Origin-Agent-Cluster":"?1","Pragma":"no-cache","Referrer-Policy":"strict-origin-when-cross-origin","Server":"nginx/1.23.2","Strict-Transport-Security":"max-age=15552000; includeSubDomains","Vary":"Accept-Encoding","X-Content-Type-Options":"nosniff","X-DNS-Prefetch-Control":"off","X-Download-Options":"noopen","X-Frame-Options":"DENY","X-Permitted-Cross-Domain-Policies":"none","X-UA-Compatible":"IE=Edge","X-XSS-Protection":"0","X-solo-application":"disneyplus-marketing"},"mimeType":"text/html","protocol":"http/1.1","remoteIPAddress":"23.44.150.44","remotePort":443,"responseTime":1.726547456930593e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_256_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disneyplus.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"304502203DA0ABCDDCF9D90E7EBFB94AEF448502C0DEA7BACC8349DB8A9DF6C5F750E1F3022100828F8E1E047B68CEEFF14D16E14C6CA511694F6416E6F22E0406826D48C1640C","status":"Verified","timestamp":1.706023785126e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100F551968BA749E63D16F0664812317C81D0AC9A23E5B39CBE00D40D30D37CA26F0221009F8FBC335F475EB6DE40D9DBCA060451E85E69D6630CED6DBADDE9C7059FB587","status":"Verified","timestamp":1.706023785204e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"304402207333FD209CD40F2B584EA279D545F2E5591EA3549DB9631FCBA7C8738C260B97022069EBF67DE6B3E71127D290A8C8D95EFFAE332E0856CFE996811CA8B22356D97A","status":"Verified","timestamp":1.706023785094e+12}],"subjectName":"*.disneyplus.com","validFrom":1705968000,"validTo":1737590399},"securityState":"secure","status":200,"statusText":"OK","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":408.295,"receiveHeadersStart":408.111,"requestTime":1925.322793,"sendEnd":0.596,"sendStart":0.479,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://www.disneyplus.com/"},"timestamp":1925.735537,"type":"Document"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456935}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[{"blockedReasons":["InvalidDomain"],"cookieLine":"x-dss-country=US; Domain=*.disneyplus.com; Path=/; HttpOnly"}],"cookiePartitionKey":{"hasCrossSiteAncestor":false,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"Cache-Control":"max-age=0, no-cache, no-store","Connection":"keep-alive","Content-Encoding":"gzip","Content-Length":"77593","Content-Security-Policy":"frame-ancestors \'self\';img-src \'self\' https://* data:;script-src \'self\' \'unsafe-inline\' \'unsafe-eval\' https://* *.disneyplus.com:*;worker-src \'self\' blob:;manifest-src \'self\' *.disneyplus.com;base-uri \'self\';font-src \'self\' https: data:;form-action \'self\';object-src \'none\';script-src-attr \'none\';style-src \'self\' https: \'unsafe-inline\';upgrade-insecure-requests","Content-Type":"text/html; charset=utf-8","Date":"Tue, 17 Sep 2024 04:30:56 GMT","Expires":"Tue, 17 Sep 2024 04:30:56 GMT","Origin-Agent-Cluster":"?1","Pragma":"no-cache","Referrer-Policy":"strict-origin-when-cross-origin","Server":"nginx/1.23.2","Set-Cookie":"x-dss-country=US; Domain=*.disneyplus.com; Path=/; HttpOnly","Strict-Transport-Security":"max-age=15552000; includeSubDomains","Vary":"Accept-Encoding","X-Content-Type-Options":"nosniff","X-DNS-Prefetch-Control":"off","X-Download-Options":"noopen","X-Frame-Options":"DENY","X-Permitted-Cross-Domain-Policies":"none","X-UA-Compatible":"IE=Edge","X-XSS-Protection":"0","X-solo-application":"disneyplus-marketing"},"headersText":"HTTP/1.1 200 OK\\r\\nContent-Type: text/html; charset=utf-8\\r\\nServer: nginx/1.23.2\\r\\nContent-Security-Policy: frame-ancestors \'self\';img-src \'self\' https://* data:;script-src \'self\' \'unsafe-inline\' \'unsafe-eval\' https://* *.disneyplus.com:*;worker-src \'self\' blob:;manifest-src \'self\' *.disneyplus.com;base-uri \'self\';font-src \'self\' https: data:;form-action \'self\';object-src \'none\';script-src-attr \'none\';style-src \'self\' https: \'unsafe-inline\';upgrade-insecure-requests\\r\\nOrigin-Agent-Cluster: ?1\\r\\nReferrer-Policy: strict-origin-when-cross-origin\\r\\nStrict-Transport-Security: max-age=15552000; includeSubDomains\\r\\nX-Content-Type-Options: nosniff\\r\\nX-DNS-Prefetch-Control: off\\r\\nX-Download-Options: noopen\\r\\nX-Frame-Options: DENY\\r\\nX-Permitted-Cross-Domain-Policies: none\\r\\nX-XSS-Protection: 0\\r\\nX-UA-Compatible: IE=Edge\\r\\nContent-Encoding: gzip\\r\\nX-solo-application: disneyplus-marketing\\r\\nContent-Length: 77593\\r\\nExpires: Tue, 17 Sep 2024 04:30:56 GMT\\r\\nCache-Control: max-age=0, no-cache, no-store\\r\\nPragma: no-cache\\r\\nDate: Tue, 17 Sep 2024 04:30:56 GMT\\r\\nConnection: keep-alive\\r\\nVary: Accept-Encoding\\r\\nSet-Cookie: x-dss-country=US; Domain=*.disneyplus.com; Path=/; HttpOnly\\r\\n\\r\\n","requestId":"939C9171ED8FE2B6C35C286E1883435F","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456939}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameNavigated","params":{"frame":{"adFrameStatus":{"adFrameType":"none"},"crossOriginIsolatedContextType":"NotIsolated","domainAndRegistry":"disneyplus.com","gatedAPIFeatures":[],"id":"3E7284AA00690624BB019FC4430314BC","loaderId":"939C9171ED8FE2B6C35C286E1883435F","mimeType":"text/html","secureContextType":"Secure","securityOrigin":"https://www.disneyplus.com","url":"https://www.disneyplus.com/"},"type":"Navigation"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456943}
{'level': 'INFO', 'message': '{"message":{"method":"Network.policyUpdated","params":{}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456944}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.758318},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/c599c52da8a32c4af829f672a5b040946ac2d49b41b018eebd86a09a21f44d2a/original",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"u=2, i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.63","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456962}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.759435},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/e7398ed4ffc16eb4eca63f549664da62cda5e6c172d799d7619f9609eac3df71/original",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"u=2, i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.64","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456962}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":397512,"encodedDataLength":0,"requestId":"939C9171ED8FE2B6C35C286E1883435F","timestamp":1925.745708}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456964}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":190,"lineNumber":84,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Origin":"https://www.disneyplus.com","Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"High","isLinkPreload":true,"isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://static-assets.bamgrid.com/fonts/inspire/Inspire-Regular.f2199f841165c4ddbafcf177da3ef974.woff2"},"requestId":"9990.59","timestamp":1925.753243,"type":"Font","wallTime":1726547456.952999}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456965}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":187,"lineNumber":85,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Origin":"https://www.disneyplus.com","Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"High","isLinkPreload":true,"isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://static-assets.bamgrid.com/fonts/inspire/Inspire-Bold.4ff15ddc93445342649194969715b0b5.woff2"},"requestId":"9990.60","timestamp":1925.754177,"type":"Font","wallTime":1726547456.953904}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456965}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":99,"lineNumber":117,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"High","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://www.datadoghq-browser-agent.com/us1/v4/datadog-rum.js"},"requestId":"9990.61","timestamp":1925.754434,"type":"Script","wallTime":1726547456.954158}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456965}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":170,"lineNumber":158,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/oneTrustConsentBundle.90d4ea260c.js"},"requestId":"9990.62","timestamp":1925.754663,"type":"Script","wallTime":1726547456.954652}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456966}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":10762,"lineNumber":185,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Medium","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/c599c52da8a32c4af829f672a5b040946ac2d49b41b018eebd86a09a21f44d2a/original"},"requestId":"9990.63","timestamp":1925.755275,"type":"Image","wallTime":1726547456.954992}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456966}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":12106,"lineNumber":185,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Medium","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/e7398ed4ffc16eb4eca63f549664da62cda5e6c172d799d7619f9609eac3df71/original"},"requestId":"9990.64","timestamp":1925.755504,"type":"Image","wallTime":1726547456.95522}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456966}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":17022,"lineNumber":185,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Medium","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/6decfd2b11e14b849b0b0cbfce963b36a13dac47c7cff42600eea6043559d32a/original"},"requestId":"9990.65","timestamp":1925.755717,"type":"Image","wallTime":1726547456.955433}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456966}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":87467,"lineNumber":185,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/5bc7286c5388eb678e209a579530895488b16071b25e7e4956e9526b00210f2e/original"},"requestId":"9990.69","timestamp":1925.756161,"type":"Image","wallTime":1726547456.955884}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456966}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":88821,"lineNumber":185,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/e4202f3ff6aabf3aff8904cb75dcf97ab17ebc74d3b6d7c7d1498748f587f3b1/original"},"requestId":"9990.70","timestamp":1925.756438,"type":"Image","wallTime":1726547456.956167}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456966}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":90147,"lineNumber":185,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/fa28d30b1356ba01fe9b34c9128757a3ac9889351f4dcd0851cf61cd6e8f9b8c/original"},"requestId":"9990.71","timestamp":1925.756666,"type":"Image","wallTime":1726547456.956385}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456966}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":91536,"lineNumber":185,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/af368171ec6cc1872094a805cbaf20999a9bb7ea7abed1d04d02d6741001c308/original"},"requestId":"9990.72","timestamp":1925.756894,"type":"Image","wallTime":1726547456.95662}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456966}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":92879,"lineNumber":185,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/2c13a1c721d0c05a8fe6b5f0607db70bf684da21657db25503ec8ae600f03672/original"},"requestId":"9990.73","timestamp":1925.760023,"type":"Image","wallTime":1726547456.959755}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456967}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":94238,"lineNumber":185,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/01274f10c21df19cef0b42b85c547afbdf4901977ce9d46f7b06c48c5c987be6/original"},"requestId":"9990.74","timestamp":1925.760222,"type":"Image","wallTime":1726547456.959938}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456967}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":185,"lineNumber":212,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/322.ace0d787afec5225e11a.js"},"requestId":"9990.75","timestamp":1925.760367,"type":"Script","wallTime":1726547456.960083}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456967}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":187,"lineNumber":213,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Medium","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/styles/960.f3b881decbe333dfe114.css"},"requestId":"9990.76","timestamp":1925.760488,"type":"Stylesheet","wallTime":1726547456.960206}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456967}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":185,"lineNumber":214,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/960.0a18b56674d234b108cb.js"},"requestId":"9990.77","timestamp":1925.760619,"type":"Script","wallTime":1726547456.960357}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456967}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":185,"lineNumber":215,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/218.4d1210286d593d83228d.js"},"requestId":"9990.78","timestamp":1925.760825,"type":"Script","wallTime":1726547456.960542}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456967}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":208,"lineNumber":216,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/marketing_script_bundle_v2.aa2876f89c04cbfdc1fe.js"},"requestId":"9990.79","timestamp":1925.760959,"type":"Script","wallTime":1726547456.960672}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456967}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":false,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.59","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":0,"connectionReused":false,"encodedDataLength":0,"fromDiskCache":true,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","access-control-allow-methods":"HEAD, GET","access-control-allow-origin":"*","access-control-max-age":"3000","age":"10964949","cache-control":"max-age=31536000","content-length":"45768","content-type":"binary/octet-stream","date":"Mon, 13 May 2024 06:41:48 GMT","etag":"\\"f2199f841165c4ddbafcf177da3ef974\\"","last-modified":"Thu, 09 May 2024 18:28:30 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Origin,Access-Control-Request-Headers,Access-Control-Request-Method","via":"1.1 19bcf0769b1328ef147a6af36ae38b82.cloudfront.net (CloudFront)","x-amz-cf-id":"gwff2WSN7GG1qU8avfvY6ptHaGNymVvCwdoLZnLX6g7XEY0v0TwybA==","x-amz-cf-pop":"LAX54-P2","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"dkRm0Wve.r.WDBDln90vy9jv3Zt.YaAn","x-cache":"Hit from cloudfront"},"mimeType":"binary/octet-stream","protocol":"h2","remoteIPAddress":"3.168.132.100","remotePort":443,"responseTime":1.726547456270005e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"unknown","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":8.512,"receiveHeadersStart":8.214,"requestTime":1925.75416,"sendEnd":0.096,"sendStart":0.096,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://static-assets.bamgrid.com/fonts/inspire/Inspire-Regular.f2199f841165c4ddbafcf177da3ef974.woff2"},"timestamp":1925.767102,"type":"Font"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456969}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":45768,"encodedDataLength":0,"requestId":"9990.59","timestamp":1925.767227}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456969}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":0,"requestId":"9990.59","timestamp":1925.765708}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456969}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":false,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.60","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":0,"connectionReused":false,"encodedDataLength":0,"fromDiskCache":true,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","access-control-allow-methods":"HEAD, GET","access-control-allow-origin":"*","access-control-max-age":"3000","age":"9360815","cache-control":"max-age=31536000","content-length":"47404","content-type":"binary/octet-stream","date":"Fri, 31 May 2024 20:17:22 GMT","etag":"\\"4ff15ddc93445342649194969715b0b5\\"","last-modified":"Tue, 14 May 2024 15:02:51 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Origin,Access-Control-Request-Headers,Access-Control-Request-Method","via":"1.1 19bcf0769b1328ef147a6af36ae38b82.cloudfront.net (CloudFront)","x-amz-cf-id":"-YQoIYE5LXG5_7d4a29oBVNOCAGDZkoLWmbPHhESlP3fFZkh8vhMxw==","x-amz-cf-pop":"LAX54-P2","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"mHgivmJvrFPL1bt8KLmQabrk3A21esyc","x-cache":"Hit from cloudfront"},"mimeType":"binary/octet-stream","protocol":"h2","remoteIPAddress":"3.168.132.100","remotePort":443,"responseTime":1.726547456253331e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"unknown","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":9.442,"receiveHeadersStart":8.048,"requestTime":1925.754546,"sendEnd":0.11,"sendStart":0.11,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://static-assets.bamgrid.com/fonts/inspire/Inspire-Bold.4ff15ddc93445342649194969715b0b5.woff2"},"timestamp":1925.767798,"type":"Font"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456969}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":47404,"encodedDataLength":0,"requestId":"9990.60","timestamp":1925.76785}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456969}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":0,"requestId":"9990.60","timestamp":1925.766238}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456969}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","age":"422885","cache-control":"max-age=365000000, immutable","content-length":"9894","content-type":"image/png","date":"Thu, 12 Sep 2024 07:02:52 GMT","etag":"\\"1e156c51b15e5abad9d13c3572666757\\"","last-modified":"Mon, 05 Aug 2024 19:53:58 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"-oweFwPr0UoUew_-rDH4a2XzKTo4sDoZE3Sz6ZDABEUEuK8UupmR1w==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.63","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456973}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","age":"4645562","cache-control":"max-age=365000000, immutable","content-length":"12852","content-type":"image/png","date":"Thu, 25 Jul 2024 10:04:55 GMT","etag":"\\"d362b14a07dc2386ec8c836b2e833e5f\\"","last-modified":"Thu, 06 Jun 2024 17:18:18 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"hj3as3S4Rh1V9IFqlj7SSMdCqMDUGSYTBk1LnTpu9L60mPOJYERZkg==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.64","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456976}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.789428},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/6decfd2b11e14b849b0b0cbfce963b36a13dac47c7cff42600eea6043559d32a/original",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"u=2, i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.65","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456990}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.63","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":368,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","age":"422885","cache-control":"max-age=365000000, immutable","content-length":"9894","content-type":"image/png","date":"Thu, 12 Sep 2024 07:02:52 GMT","etag":"\\"1e156c51b15e5abad9d13c3572666757\\"","last-modified":"Mon, 05 Aug 2024 19:53:58 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"-oweFwPr0UoUew_-rDH4a2XzKTo4sDoZE3Sz6ZDABEUEuK8UupmR1w==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"image/png","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547456971658e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":13.788,"receiveHeadersStart":13.615,"requestTime":1925.758318,"sendEnd":5.658,"sendStart":3.647,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/c599c52da8a32c4af829f672a5b040946ac2d49b41b018eebd86a09a21f44d2a/original"},"timestamp":1925.788766,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456990}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":9894,"encodedDataLength":0,"requestId":"9990.63","timestamp":1925.788806}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456990}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":10280,"requestId":"9990.63","timestamp":1925.772881}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456990}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.64","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":371,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","age":"4645562","cache-control":"max-age=365000000, immutable","content-length":"12852","content-type":"image/png","date":"Thu, 25 Jul 2024 10:04:55 GMT","etag":"\\"d362b14a07dc2386ec8c836b2e833e5f\\"","last-modified":"Thu, 06 Jun 2024 17:18:18 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"hj3as3S4Rh1V9IFqlj7SSMdCqMDUGSYTBk1LnTpu9L60mPOJYERZkg==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"image/png","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547456974207e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":15.202,"receiveHeadersStart":15.049,"requestTime":1925.759435,"sendEnd":4.544,"sendStart":2.841,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/e7398ed4ffc16eb4eca63f549664da62cda5e6c172d799d7619f9609eac3df71/original"},"timestamp":1925.789876,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456992}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":12852,"encodedDataLength":0,"requestId":"9990.64","timestamp":1925.789934}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456992}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":13241,"requestId":"9990.64","timestamp":1925.775501}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456992}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.791367},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/app/build/generic/styles/960.f3b881decbe333dfe114.css",":scheme":"https","accept":"text/css,*/*;q=0.1","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"u=2","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"style","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.76","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456992}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":78754,"requestId":"939C9171ED8FE2B6C35C286E1883435F","timestamp":1925.73648}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456993}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.754852},"headers":{":authority":"www.datadoghq-browser-agent.com",":method":"GET",":path":"/us1/v4/datadog-rum.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"u=1","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.61","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547456999}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","age":"422376","cache-control":"max-age=365000000, immutable","content-length":"247708","content-type":"image/jpeg","date":"Thu, 12 Sep 2024 07:11:21 GMT","etag":"\\"afd0cfb8d3468d0dc573024255abcb1c\\"","last-modified":"Tue, 03 Sep 2024 20:49:24 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"cUZvdDtsoI1vk9Rbh4m26S6t7j9Iue5l9BkiOA_0a9xGoBPQpj3JrA==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.65","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457001}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"45378","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"text/css","date":"Mon, 16 Sep 2024 15:54:39 GMT","etag":"W/\\"017f2a647f599087f466ad0ed7ed66d1\\"","last-modified":"Sat, 14 Sep 2024 00:19:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"sMnxl1rYm_qD017HNyq8KFP7cvHznb1VvFgPIoG1_zRehjFqvp8EWA==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"zBBSUI4aJ6dj3u2LF1WpFDmhjMMM1qLS","x-cache":"Hit from cloudfront"},"requestId":"9990.76","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457001}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.76","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":459,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"45378","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"text/css","date":"Mon, 16 Sep 2024 15:54:39 GMT","etag":"W/\\"017f2a647f599087f466ad0ed7ed66d1\\"","last-modified":"Sat, 14 Sep 2024 00:19:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"sMnxl1rYm_qD017HNyq8KFP7cvHznb1VvFgPIoG1_zRehjFqvp8EWA==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"zBBSUI4aJ6dj3u2LF1WpFDmhjMMM1qLS","x-cache":"Hit from cloudfront"},"mimeType":"text/css","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547457001071e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":10.125,"receiveHeadersStart":9.969,"requestTime":1925.791367,"sendEnd":0.515,"sendStart":0.343,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/styles/960.f3b881decbe333dfe114.css"},"timestamp":1925.802535,"type":"Stylesheet"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457003}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":15155,"encodedDataLength":0,"requestId":"9990.76","timestamp":1925.80272}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457003}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":0,"encodedDataLength":2142,"requestId":"9990.76","timestamp":1925.803186}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457003}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":2601,"requestId":"9990.76","timestamp":1925.802541}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457003}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.65","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":370,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","age":"422376","cache-control":"max-age=365000000, immutable","content-length":"247708","content-type":"image/jpeg","date":"Thu, 12 Sep 2024 07:11:21 GMT","etag":"\\"afd0cfb8d3468d0dc573024255abcb1c\\"","last-modified":"Tue, 03 Sep 2024 20:49:24 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"cUZvdDtsoI1vk9Rbh4m26S6t7j9Iue5l9BkiOA_0a9xGoBPQpj3JrA==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"image/jpeg","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547457000381e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":11.385,"receiveHeadersStart":11.225,"requestTime":1925.789428,"sendEnd":0.529,"sendStart":0.351,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/6decfd2b11e14b849b0b0cbfce963b36a13dac47c7cff42600eea6043559d32a/original"},"timestamp":1925.808087,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457008}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":65094,"encodedDataLength":0,"requestId":"9990.65","timestamp":1925.808139}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457008}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":32732,"encodedDataLength":97934,"requestId":"9990.65","timestamp":1925.810616}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457010}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"56","cache-control":"max-age=14400, s-maxage=60","content-encoding":"br","content-type":"application/javascript","date":"Tue, 17 Sep 2024 04:30:57 GMT","etag":"W/\\"2630b3d7ad4a41fac67742216e506d83\\"","last-modified":"Mon, 09 Oct 2023 09:24:57 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 5ebfb3ebd854803fa242c7a39fbcd92c.cloudfront.net (CloudFront)","x-amz-cf-id":"y528eYJKAqPdR9lhBRi-ZiMMq05nBpJmKRdboX1mg9A58BSr5r6Dlg==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.61","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457010}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.61","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":400,"connectionReused":false,"encodedDataLength":406,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"56","cache-control":"max-age=14400, s-maxage=60","content-encoding":"br","content-type":"application/javascript","date":"Tue, 17 Sep 2024 04:30:57 GMT","etag":"W/\\"2630b3d7ad4a41fac67742216e506d83\\"","last-modified":"Mon, 09 Oct 2023 09:24:57 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 5ebfb3ebd854803fa242c7a39fbcd92c.cloudfront.net (CloudFront)","x-amz-cf-id":"y528eYJKAqPdR9lhBRi-ZiMMq05nBpJmKRdboX1mg9A58BSr5r6Dlg==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.86.180","remotePort":443,"responseTime":1.726547457010139e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"DigiCert Global G2 TLS RSA SHA256 2020 CA1","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.datadoghq-browser-agent.com","datadoghq-browser-agent.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B726FB146A42EC9D85CA89F079C3A238697C677E3C3AC8729A0166C1AF306329022100CCBD5FFBB8C669B2BF6DC1FB3B2928A5EDBC735DBC868BFD510855B0B276305C","status":"Verified","timestamp":1.722301147681e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"304402206ACF6E5671792C972656A4AAB463ABA2ADA3A5FF9CC5968F1A7E515E4B7A73E702200DB6D881B9E9CE0EB7C59BF5177591582255698D75B196166B54E17FEA97E90B","status":"Verified","timestamp":1.722301147545e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"304502206A1109C409AA40A9598F63938640C0036A3749D3674FF6B464B6063CC38C7DF9022100CAD3AAEC1429337803A56518854E300D9EEC1AFF89D6276CF643F323C0FC6B16","status":"Verified","timestamp":1.722301147561e+12}],"subjectName":"*.datadoghq-browser-agent.com","validFrom":1722297600,"validTo":1754265599},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":44.409,"connectStart":21.758,"dnsEnd":21.653,"dnsStart":0.481,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":55.832,"receiveHeadersStart":55.562,"requestTime":1925.754852,"sendEnd":44.769,"sendStart":44.581,"sslEnd":44.402,"sslStart":31.084,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://www.datadoghq-browser-agent.com/us1/v4/datadog-rum.js"},"timestamp":1925.813573,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457015}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":45943,"encodedDataLength":0,"requestId":"9990.61","timestamp":1925.813641}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457015}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":65536,"encodedDataLength":81920,"requestId":"9990.65","timestamp":1925.816796}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457017}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":16294,"encodedDataLength":0,"requestId":"9990.65","timestamp":1925.817261}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457017}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":16366,"encodedDataLength":16384,"requestId":"9990.65","timestamp":1925.820351}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457020}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":51686,"encodedDataLength":51749,"requestId":"9990.65","timestamp":1925.824856}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457026}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":248357,"requestId":"9990.65","timestamp":1925.823958}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457026}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":65536,"encodedDataLength":48482,"requestId":"9990.61","timestamp":1925.826774}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457026}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.826353},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/app/build/generic/scripts/oneTrustConsentBundle.90d4ea260c.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.62","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457027}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":41677,"encodedDataLength":0,"requestId":"9990.61","timestamp":1925.830335}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457030}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.832582},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/5bc7286c5388eb678e209a579530895488b16071b25e7e4956e9526b00210f2e/original",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.69","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457033}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":48888,"requestId":"9990.61","timestamp":1925.822257}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457033}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"359840","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Fri, 13 Sep 2024 00:33:38 GMT","etag":"W/\\"4e557d72ce19d8d4c0890b79452b2f9c\\"","last-modified":"Thu, 12 Sep 2024 23:41:11 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"zHnzH6rJGPluERJ7NdLeP9qVU-KTHzctJm8gylv7Vn0JEDd-wSX8dA==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"soEQoUI8fyobdy1YxVdEI7FtA7Tq4Mu4","x-cache":"Hit from cloudfront"},"requestId":"9990.62","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457037}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","age":"5478036","cache-control":"max-age=365000000, immutable","content-length":"270304","content-type":"image/png","date":"Mon, 15 Jul 2024 18:50:22 GMT","etag":"\\"70d9e224562b580bd9f448543ee6a226\\"","last-modified":"Fri, 21 Jun 2024 14:38:19 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"WI2fWCTcGgNYAqsx_8AiiAaE_aqiF6YHqXueBfeKX7rSasxCXMJE0A==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.69","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457044}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://disney.api.edge.bamgrid.com/graph/v1/device/graphql","hasUserGesture":false,"initiator":{"requestId":"9990.103","type":"preflight","url":"https://disney.api.edge.bamgrid.com/graph/v1/device/graphql"},"loaderId":"","redirectHasExtraInfo":false,"request":{"headers":{"Accept":"*/*","Access-Control-Request-Headers":"authorization,content-type,x-application-version,x-bamsdk-client-id,x-bamsdk-platform,x-bamsdk-platform-id,x-bamsdk-version,x-bamtech-wpnx-mlp-identifier,x-bamtech-wpnx-mlp-locale","Access-Control-Request-Method":"POST","Origin":"https://www.disneyplus.com","Sec-Fetch-Mode":"cors","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"initialPriority":"High","method":"OPTIONS","referrerPolicy":"strict-origin-when-cross-origin","url":"https://disney.api.edge.bamgrid.com/graph/v1/device/graphql"},"requestId":"5D60B9F7D02C7B80F4BCAB8B8FF213BB","timestamp":1925.895489,"type":"Other","wallTime":1726547457.095195}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457097}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.89782},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/e4202f3ff6aabf3aff8904cb75dcf97ab17ebc74d3b6d7c7d1498748f587f3b1/original",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.70","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457100}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.898497},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/fa28d30b1356ba01fe9b34c9128757a3ac9889351f4dcd0851cf61cd6e8f9b8c/original",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.71","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457101}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.898878},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/af368171ec6cc1872094a805cbaf20999a9bb7ea7abed1d04d02d6741001c308/original",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.72","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457101}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.899238},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/2c13a1c721d0c05a8fe6b5f0607db70bf684da21657db25503ec8ae600f03672/original",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.73","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457103}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.899621},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/01274f10c21df19cef0b42b85c547afbdf4901977ce9d46f7b06c48c5c987be6/original",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.74","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457103}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.900214},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/app/build/generic/scripts/322.ace0d787afec5225e11a.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.75","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457103}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.900584},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/app/build/generic/scripts/960.0a18b56674d234b108cb.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.77","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457103}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.901222},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/app/build/generic/scripts/218.4d1210286d593d83228d.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.78","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457104}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"stack":{"callFrames":[{"columnNumber":44122,"functionName":"Lr.Cr","lineNumber":0,"scriptId":"28","url":"https://www.datadoghq-browser-agent.com/us1/v4/datadog-rum.js"},{"columnNumber":42419,"functionName":"o","lineNumber":0,"scriptId":"28","url":"https://www.datadoghq-browser-agent.com/us1/v4/datadog-rum.js"},{"columnNumber":16812,"functionName":"","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":9674,"functionName":"u","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":9427,"functionName":"","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":10037,"functionName":"","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":15604,"functionName":"h","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":15807,"functionName":"a","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":15866,"functionName":"","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":15747,"functionName":"","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":18414,"functionName":"","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":20404,"functionName":"","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":9674,"functionName":"u","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":9427,"functionName":"","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":10037,"functionName":"","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":15604,"functionName":"h","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":15807,"functionName":"a","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":15866,"functionName":"","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":15747,"functionName":"","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":21562,"functionName":"","lineNumber":142,"scriptId":"33","url":"https://www.disneyplus.com/"},{"columnNumber":12262,"functionName":"","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"},{"columnNumber":6161,"functionName":"s","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"},{"columnNumber":5914,"functionName":"","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"},{"columnNumber":6524,"functionName":"","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"},{"columnNumber":11396,"functionName":"E","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"},{"columnNumber":13212,"functionName":"a","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"},{"columnNumber":13271,"functionName":"","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"},{"columnNumber":13152,"functionName":"","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"},{"columnNumber":13313,"functionName":"","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"},{"columnNumber":13360,"functionName":"9544","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"},{"columnNumber":205,"functionName":"t","lineNumber":88,"scriptId":"24","url":"https://www.disneyplus.com/"},{"columnNumber":13473,"functionName":"","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"},{"columnNumber":487,"functionName":"t.O","lineNumber":88,"scriptId":"24","url":"https://www.disneyplus.com/"},{"columnNumber":13493,"functionName":"","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"},{"columnNumber":1355,"functionName":"r","lineNumber":88,"scriptId":"24","url":"https://www.disneyplus.com/"},{"columnNumber":318,"functionName":"","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"},{"columnNumber":170,"functionName":"","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"},{"columnNumber":235,"functionName":"","lineNumber":145,"scriptId":"34","url":"https://www.disneyplus.com/"}]},"type":"script"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"hasPostData":true,"headers":{"Content-Type":"application/json","Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","X-BAMSDK-Platform-Id":"browser","authorization":"Bearer ZGlzbmV5JmJyb3dzZXImMS4wLjA.Cu56AgSfBTDag5NiRA81oLHkDZfu5L3CKadnefEAY84","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","x-application-version":"b928d05b","x-bamsdk-client-id":"disney-svod-3d9324fc","x-bamsdk-platform":"javascript/linux}/chrome","x-bamsdk-version":"b928d05b-dplus-mlp","x-bamtech-wpnx-mlp-identifier":"/","x-bamtech-wpnx-mlp-locale":"en-us"},"initialPriority":"High","isSameSite":false,"method":"POST","mixedContentType":"none","postData":"{\\"operationName\\":\\"registerDevice\\",\\"query\\":\\"mutation registerDevice($input: RegisterDeviceInput!) {\\\\n            registerDevice(registerDevice: $input) {\\\\n                grant {\\\\n                  grantType\\\\n                  assertion\\\\n                },\\\\n                activeSession {\\\\n                  partnerName\\\\n                  profile {\\\\n                    id\\\\n                  }\\\\n                }\\\\n            }\\\\n        }\\",\\"variables\\":{\\"input\\":{\\"deviceFamily\\":\\"browser\\",\\"applicationRuntime\\":\\"chrome\\",\\"deviceProfile\\":\\"linux\\",\\"deviceLanguage\\":\\"en\\",\\"devicePlatformId\\":\\"browser\\",\\"attributes\\":{\\"brand\\":\\"web\\",\\"browserName\\":\\"chrome\\",\\"browserVersion\\":\\"128.0.0.0\\",\\"manufacturer\\":\\"n/a\\",\\"operatingSystem\\":\\"linux\\",\\"operatingSystemVersion\\":\\"86.64\\"}}}}","postDataEntries":[{"bytes":"eyJvcGVyYXRpb25OYW1lIjoicmVnaXN0ZXJEZXZpY2UiLCJxdWVyeSI6Im11dGF0aW9uIHJlZ2lzdGVyRGV2aWNlKCRpbnB1dDogUmVnaXN0ZXJEZXZpY2VJbnB1dCEpIHtcbiAgICAgICAgICAgIHJlZ2lzdGVyRGV2aWNlKHJlZ2lzdGVyRGV2aWNlOiAkaW5wdXQpIHtcbiAgICAgICAgICAgICAgICBncmFudCB7XG4gICAgICAgICAgICAgICAgICBncmFudFR5cGVcbiAgICAgICAgICAgICAgICAgIGFzc2VydGlvblxuICAgICAgICAgICAgICAgIH0sXG4gICAgICAgICAgICAgICAgYWN0aXZlU2Vzc2lvbiB7XG4gICAgICAgICAgICAgICAgICBwYXJ0bmVyTmFtZVxuICAgICAgICAgICAgICAgICAgcHJvZmlsZSB7XG4gICAgICAgICAgICAgICAgICAgIGlkXG4gICAgICAgICAgICAgICAgICB9XG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfVxuICAgICAgICB9IiwidmFyaWFibGVzIjp7ImlucHV0Ijp7ImRldmljZUZhbWlseSI6ImJyb3dzZXIiLCJhcHBsaWNhdGlvblJ1bnRpbWUiOiJjaHJvbWUiLCJkZXZpY2VQcm9maWxlIjoibGludXgiLCJkZXZpY2VMYW5ndWFnZSI6ImVuIiwiZGV2aWNlUGxhdGZvcm1JZCI6ImJyb3dzZXIiLCJhdHRyaWJ1dGVzIjp7ImJyYW5kIjoid2ViIiwiYnJvd3Nlck5hbWUiOiJjaHJvbWUiLCJicm93c2VyVmVyc2lvbiI6IjEyOC4wLjAuMCIsIm1hbnVmYWN0dXJlciI6Im4vYSIsIm9wZXJhdGluZ1N5c3RlbSI6ImxpbnV4Iiwib3BlcmF0aW5nU3lzdGVtVmVyc2lvbiI6Ijg2LjY0In19fX0="}],"referrerPolicy":"strict-origin-when-cross-origin","url":"https://disney.api.edge.bamgrid.com/graph/v1/device/graphql"},"requestId":"9990.103","timestamp":1925.894404,"type":"Fetch","wallTime":1726547457.094617}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457105}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.903649},"headers":{":authority":"prod-static.disney-plus.net",":method":"GET",":path":"/us-east-1/disneyPlus/app/build/generic/scripts/marketing_script_bundle_v2.aa2876f89c04cbfdc1fe.js",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.79","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457105}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.69","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":372,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","age":"5478036","cache-control":"max-age=365000000, immutable","content-length":"270304","content-type":"image/png","date":"Mon, 15 Jul 2024 18:50:22 GMT","etag":"\\"70d9e224562b580bd9f448543ee6a226\\"","last-modified":"Fri, 21 Jun 2024 14:38:19 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"WI2fWCTcGgNYAqsx_8AiiAaE_aqiF6YHqXueBfeKX7rSasxCXMJE0A==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"image/png","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547457042834e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":10.701,"receiveHeadersStart":10.527,"requestTime":1925.832582,"sendEnd":0.879,"sendStart":0.368,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/5bc7286c5388eb678e209a579530895488b16071b25e7e4956e9526b00210f2e/original"},"timestamp":1925.904363,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457110}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":270304,"encodedDataLength":0,"requestId":"9990.69","timestamp":1925.90444}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457110}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":0,"encodedDataLength":270601,"requestId":"9990.69","timestamp":1925.905523}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457110}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":270973,"requestId":"9990.69","timestamp":1925.850086}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457110}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.62","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":471,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"359840","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Fri, 13 Sep 2024 00:33:38 GMT","etag":"W/\\"4e557d72ce19d8d4c0890b79452b2f9c\\"","last-modified":"Thu, 12 Sep 2024 23:41:11 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"zHnzH6rJGPluERJ7NdLeP9qVU-KTHzctJm8gylv7Vn0JEDd-wSX8dA==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"soEQoUI8fyobdy1YxVdEI7FtA7Tq4Mu4","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.72654745703716e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":11.248,"receiveHeadersStart":11.082,"requestTime":1925.826353,"sendEnd":1.18,"sendStart":0.825,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/oneTrustConsentBundle.90d4ea260c.js"},"timestamp":1925.9071,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457111}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":2093,"encodedDataLength":0,"requestId":"9990.62","timestamp":1925.907174}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457111}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","age":"8537958","cache-control":"max-age=365000000, immutable","content-length":"56337","content-type":"image/jpeg","date":"Mon, 10 Jun 2024 08:51:40 GMT","etag":"\\"8ffdf23404a992f9297f1ed17c7ff805\\"","last-modified":"Tue, 21 May 2024 18:03:51 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"242_5sUH_URHbgWnhfmw3IqMbEN9qvxSYoRpuuMBKVNuOXPMnkqkpg==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.70","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457112}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"45379","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:54:39 GMT","etag":"W/\\"20785cc1664b230c5bf528b8a6b96e17\\"","last-modified":"Sat, 14 Sep 2024 00:19:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"ijVvmtFwjWFnrNmdDabbiiI8nNqlHmbQzysrTUT7AmajMlIAug2aFQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"PMVfl.yzBA3l_.dtwR6XLEUPrOwpTAcL","x-cache":"Hit from cloudfront"},"requestId":"9990.75","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457116}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","age":"9038605","cache-control":"max-age=365000000, immutable","content-length":"74960","content-type":"image/jpeg","date":"Tue, 04 Jun 2024 13:47:33 GMT","etag":"\\"43fcb869d4bcdb5534c39fc432f7bf8c\\"","last-modified":"Thu, 25 Apr 2024 20:20:45 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"LtBp1c2STqVeWj9o5XAm11l9BJScwTn7X0AySPBnE7EzpMJ4maOd0Q==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.71","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457117}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","age":"8354793","cache-control":"max-age=365000000, immutable","content-length":"146546","content-type":"image/jpeg","date":"Wed, 12 Jun 2024 11:44:25 GMT","etag":"\\"881ffc2b9246c26d09bfa4b1a46b0004\\"","last-modified":"Thu, 25 Apr 2024 21:11:00 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"VH3SS9XSj-RKcIE2wW6uGys7skJC5MBkkC65GtPZjj5jX2FpHlLQdg==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.72","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457118}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","age":"8351026","cache-control":"max-age=365000000, immutable","content-length":"184743","content-type":"image/jpeg","date":"Wed, 12 Jun 2024 12:47:12 GMT","etag":"\\"cfa87d69cc87f17a2c886cb28a273681\\"","last-modified":"Tue, 14 May 2024 16:39:03 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"o25YjIcDTl9o66UMa0aBvMCUdV9ZSCH3Ugtqx_T5dHEME3lZwUTPew==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.73","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457120}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"45379","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:54:39 GMT","etag":"W/\\"7e0ffba5e8489521d26f2e8b5a349095\\"","last-modified":"Sat, 14 Sep 2024 00:19:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"97bm7nTVCgKABbNqVTbNuukBLbd0Zt17d8-H6fbrFYrh3Mj4q0g5pA==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"un8pmgOdOm66_k9jEs6ZcwSQ7E4f49tj","x-cache":"Hit from cloudfront"},"requestId":"9990.77","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457123}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"45379","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:54:39 GMT","etag":"W/\\"bb6994ab6efeb1728ce2f51cd3c266cf\\"","last-modified":"Sat, 14 Sep 2024 00:19:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"X6w-uX6swyyWIrxZs2YuAWYNAnspcwIVHkfq6_Q734Jnnav26Kl2EA==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"OXvWuxfBecb6mb0NPrM1ACgGuQo9YtTw","x-cache":"Hit from cloudfront"},"requestId":"9990.78","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457124}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.70","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":373,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","age":"8537958","cache-control":"max-age=365000000, immutable","content-length":"56337","content-type":"image/jpeg","date":"Mon, 10 Jun 2024 08:51:40 GMT","etag":"\\"8ffdf23404a992f9297f1ed17c7ff805\\"","last-modified":"Tue, 21 May 2024 18:03:51 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"242_5sUH_URHbgWnhfmw3IqMbEN9qvxSYoRpuuMBKVNuOXPMnkqkpg==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"image/jpeg","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547457111613e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":14.314,"receiveHeadersStart":14.067,"requestTime":1925.89782,"sendEnd":4.452,"sendStart":2.134,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/e4202f3ff6aabf3aff8904cb75dcf97ab17ebc74d3b6d7c7d1498748f587f3b1/original"},"timestamp":1925.922289,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457126}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":56337,"encodedDataLength":0,"requestId":"9990.70","timestamp":1925.922365}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457126}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":56773,"requestId":"9990.70","timestamp":1925.914301}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457126}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"age":"45379","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:54:39 GMT","etag":"W/\\"4971965364c37e7c38afd9fc89b79b99\\"","last-modified":"Sat, 14 Sep 2024 00:19:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"IgAZSywD6Eipbzrnk_V8GJhiK8FOVBnfHADEunNR879SI2AZ64pehQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"NE5PK7aP08lsm5K3R1a_lo9UKMWuaaNC","x-cache":"Hit from cloudfront"},"requestId":"9990.79","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457127}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.71","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":371,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","age":"9038605","cache-control":"max-age=365000000, immutable","content-length":"74960","content-type":"image/jpeg","date":"Tue, 04 Jun 2024 13:47:33 GMT","etag":"\\"43fcb869d4bcdb5534c39fc432f7bf8c\\"","last-modified":"Thu, 25 Apr 2024 20:20:45 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"LtBp1c2STqVeWj9o5XAm11l9BJScwTn7X0AySPBnE7EzpMJ4maOd0Q==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"image/jpeg","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547457114244e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":16.248,"receiveHeadersStart":15.974,"requestTime":1925.898497,"sendEnd":3.777,"sendStart":2.487,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/fa28d30b1356ba01fe9b34c9128757a3ac9889351f4dcd0851cf61cd6e8f9b8c/original"},"timestamp":1925.928156,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457129}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":74960,"encodedDataLength":0,"requestId":"9990.71","timestamp":1925.928222}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457129}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":0,"encodedDataLength":75050,"requestId":"9990.71","timestamp":1925.928922}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457129}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":75421,"requestId":"9990.71","timestamp":1925.920571}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457129}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","age":"8351026","cache-control":"max-age=365000000, immutable","content-length":"66887","content-type":"image/jpeg","date":"Wed, 12 Jun 2024 12:47:12 GMT","etag":"\\"20ffb3f709fbcbb2b26add024203886b\\"","last-modified":"Thu, 25 Apr 2024 20:20:45 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"bKEWelP1GDE8Nm7s8YN3bbY6nHjbUS82MELlsHYfWZGwPQOi_CnKaQ==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.74","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457130}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.72","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":373,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","age":"8354793","cache-control":"max-age=365000000, immutable","content-length":"146546","content-type":"image/jpeg","date":"Wed, 12 Jun 2024 11:44:25 GMT","etag":"\\"881ffc2b9246c26d09bfa4b1a46b0004\\"","last-modified":"Thu, 25 Apr 2024 21:11:00 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"VH3SS9XSj-RKcIE2wW6uGys7skJC5MBkkC65GtPZjj5jX2FpHlLQdg==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"image/jpeg","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547457117176e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":18.707,"receiveHeadersStart":18.58,"requestTime":1925.898878,"sendEnd":3.398,"sendStart":2.626,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/af368171ec6cc1872094a805cbaf20999a9bb7ea7abed1d04d02d6741001c308/original"},"timestamp":1925.931351,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457133}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":146546,"encodedDataLength":0,"requestId":"9990.72","timestamp":1925.931418}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457133}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":0,"encodedDataLength":146708,"requestId":"9990.72","timestamp":1925.932715}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457134}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":147081,"requestId":"9990.72","timestamp":1925.929253}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457134}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.73","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":371,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","age":"8351026","cache-control":"max-age=365000000, immutable","content-length":"184743","content-type":"image/jpeg","date":"Wed, 12 Jun 2024 12:47:12 GMT","etag":"\\"cfa87d69cc87f17a2c886cb28a273681\\"","last-modified":"Tue, 14 May 2024 16:39:03 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"o25YjIcDTl9o66UMa0aBvMCUdV9ZSCH3Ugtqx_T5dHEME3lZwUTPew==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"image/jpeg","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547457119776e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":20.954,"receiveHeadersStart":20.817,"requestTime":1925.899238,"sendEnd":3.04,"sendStart":2.378,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/2c13a1c721d0c05a8fe6b5f0607db70bf684da21657db25503ec8ae600f03672/original"},"timestamp":1925.933202,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457138}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":184743,"encodedDataLength":0,"requestId":"9990.73","timestamp":1925.933259}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457138}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":0,"encodedDataLength":184950,"requestId":"9990.73","timestamp":1925.934945}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457138}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":185321,"requestId":"9990.73","timestamp":1925.932571}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457138}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.74","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":371,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","age":"8351026","cache-control":"max-age=365000000, immutable","content-length":"66887","content-type":"image/jpeg","date":"Wed, 12 Jun 2024 12:47:12 GMT","etag":"\\"20ffb3f709fbcbb2b26add024203886b\\"","last-modified":"Thu, 25 Apr 2024 20:20:45 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"bKEWelP1GDE8Nm7s8YN3bbY6nHjbUS82MELlsHYfWZGwPQOi_CnKaQ==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"image/jpeg","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547457129855e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":30.64,"receiveHeadersStart":30.515,"requestTime":1925.899621,"sendEnd":2.658,"sendStart":2.072,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/01274f10c21df19cef0b42b85c547afbdf4901977ce9d46f7b06c48c5c987be6/original"},"timestamp":1925.935424,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457138}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":66887,"encodedDataLength":0,"requestId":"9990.74","timestamp":1925.935478}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457138}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":0,"encodedDataLength":66968,"requestId":"9990.74","timestamp":1925.936062}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457138}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":67339,"requestId":"9990.74","timestamp":1925.933439}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457138}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":1375,"requestId":"9990.62","timestamp":1925.838458}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457138}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.75","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":468,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"45379","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:54:39 GMT","etag":"W/\\"20785cc1664b230c5bf528b8a6b96e17\\"","last-modified":"Sat, 14 Sep 2024 00:19:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"ijVvmtFwjWFnrNmdDabbiiI8nNqlHmbQzysrTUT7AmajMlIAug2aFQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"PMVfl.yzBA3l_.dtwR6XLEUPrOwpTAcL","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547457112604e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":12.858,"receiveHeadersStart":12.666,"requestTime":1925.900214,"sendEnd":2.204,"sendStart":1.848,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/322.ace0d787afec5225e11a.js"},"timestamp":1925.936887,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457143}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":764277,"encodedDataLength":0,"requestId":"9990.75","timestamp":1925.936964}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457144}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.77","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":469,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"45379","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:54:39 GMT","etag":"W/\\"7e0ffba5e8489521d26f2e8b5a349095\\"","last-modified":"Sat, 14 Sep 2024 00:19:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"97bm7nTVCgKABbNqVTbNuukBLbd0Zt17d8-H6fbrFYrh3Mj4q0g5pA==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"un8pmgOdOm66_k9jEs6ZcwSQ7E4f49tj","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547457122004e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":21.859,"receiveHeadersStart":21.699,"requestTime":1925.900584,"sendEnd":1.836,"sendStart":1.569,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/960.0a18b56674d234b108cb.js"},"timestamp":1925.952255,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457155}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":13108,"encodedDataLength":0,"requestId":"9990.77","timestamp":1925.952332}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457155}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.78","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":469,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"45379","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:54:39 GMT","etag":"W/\\"bb6994ab6efeb1728ce2f51cd3c266cf\\"","last-modified":"Sat, 14 Sep 2024 00:19:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"X6w-uX6swyyWIrxZs2YuAWYNAnspcwIVHkfq6_Q734Jnnav26Kl2EA==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"OXvWuxfBecb6mb0NPrM1ACgGuQo9YtTw","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547457123287e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":22.474,"receiveHeadersStart":22.343,"requestTime":1925.901222,"sendEnd":1.199,"sendStart":1.007,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/218.4d1210286d593d83228d.js"},"timestamp":1925.956049,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457162}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":52266,"encodedDataLength":0,"requestId":"9990.78","timestamp":1925.956178}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457162}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.79","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":148,"connectionReused":true,"encodedDataLength":469,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"age":"45379","cache-control":"max-age=604800","content-encoding":"gzip","content-type":"application/javascript","date":"Mon, 16 Sep 2024 15:54:39 GMT","etag":"W/\\"4971965364c37e7c38afd9fc89b79b99\\"","last-modified":"Sat, 14 Sep 2024 00:19:34 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 f90f6e9169afe2a4dc7dc7dbb34b81ca.cloudfront.net (CloudFront)","x-amz-cf-id":"IgAZSywD6Eipbzrnk_V8GJhiK8FOVBnfHADEunNR879SI2AZ64pehQ==","x-amz-cf-pop":"PHX52-P1","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"NE5PK7aP08lsm5K3R1a_lo9UKMWuaaNC","x-cache":"Hit from cloudfront"},"mimeType":"application/javascript","protocol":"h2","remoteIPAddress":"18.238.85.122","remotePort":443,"responseTime":1.726547457125627e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disney-plus.net","disney-plus.net"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Xenon2025h1\' log","logId":"CF1156EED52E7CAFF3875BD9692E9BE91A71674AB017ECAC01D25B77CECC3B08","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100CD0F983D86E1B5D03B23570CB05E6EE0E73BE6C5B60AF2A20732D4C7A868C066022100E24BD199C42B99401753A3CBF48FD754B042BC86508F3885990078B698BD0E98","status":"Verified","timestamp":1.708103893106e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2025h1\'","logId":"A2E30AE445EFBDAD9B7E38ED47677753D7825B8494D72B5E1B2CC4B950A447E7","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3044022023D20CB599C80DD88708D7B5D7FFCEDD5F4500BD87208388A25E7E3F0A99639602206AAC649BDD1F8668381482E4AECD1F3AC34CF3C23CE796CB615F55D65C9D52C8","status":"Verified","timestamp":1.708103893327e+12},{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B74DCABF6031C71AF8FA6D00E87B33EA8367B56213DB42627F51D330A5135DE7022100C90895D2BDA1EC6A93B0E3541EC25C04043CBEA78BE57B67E612033905C9EE7B","status":"Verified","timestamp":1.708103893152e+12}],"subjectName":"*.disney-plus.net","validFrom":1708041600,"validTo":1739663999},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":22.413,"receiveHeadersStart":22.258,"requestTime":1925.903649,"sendEnd":0.613,"sendStart":0.45,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/marketing_script_bundle_v2.aa2876f89c04cbfdc1fe.js"},"timestamp":1925.96176,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457163}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":81665,"encodedDataLength":0,"requestId":"9990.79","timestamp":1925.961849}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457163}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.974122},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/bf5d7853585919974955302b636e8680d8cff37cd12c87b86bc882e4e60ebc67/original",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.139","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":76101,"lineNumber":185,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/bf5d7853585919974955302b636e8680d8cff37cd12c87b86bc882e4e60ebc67/original"},"requestId":"9990.139","timestamp":1925.973637,"type":"Image","wallTime":1726547457.17337}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457175}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":5372,"requestId":"9990.77","timestamp":1925.923377}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457177}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":13729,"requestId":"9990.78","timestamp":1925.925695}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457177}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":0,"encodedDataLength":14828,"requestId":"9990.79","timestamp":1925.976834}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457177}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":15297,"requestId":"9990.79","timestamp":1925.928501}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457177}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","age":"4646402","cache-control":"max-age=365000000, immutable","content-length":"13188","content-type":"image/png","date":"Thu, 25 Jul 2024 09:50:55 GMT","etag":"\\"f1d38ccc50c2180746802326f478d41a\\"","last-modified":"Tue, 16 Jul 2024 16:05:33 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"JeLUzYAVnGsTquKL65yyphpjUBeQZKqLUpTs0mcvuiOVNbX5rUy8rA==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.139","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457184}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1925.895526},"headers":{":authority":"disney.api.edge.bamgrid.com",":method":"OPTIONS",":path":"/graph/v1/device/graphql",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","access-control-request-headers":"authorization,content-type,x-application-version,x-bamsdk-client-id,x-bamsdk-platform,x-bamsdk-platform-id,x-bamsdk-version,x-bamtech-wpnx-mlp-identifier,x-bamtech-wpnx-mlp-locale","access-control-request-method":"POST","origin":"https://www.disneyplus.com","priority":"u=1, i","referer":"https://www.disneyplus.com/","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"5D60B9F7D02C7B80F4BCAB8B8FF213BB","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457187}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.139","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":371,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","age":"4646402","cache-control":"max-age=365000000, immutable","content-length":"13188","content-type":"image/png","date":"Thu, 25 Jul 2024 09:50:55 GMT","etag":"\\"f1d38ccc50c2180746802326f478d41a\\"","last-modified":"Tue, 16 Jul 2024 16:05:33 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"JeLUzYAVnGsTquKL65yyphpjUBeQZKqLUpTs0mcvuiOVNbX5rUy8rA==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"image/png","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547457183936e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":10.259,"receiveHeadersStart":10.088,"requestTime":1925.974122,"sendEnd":0.705,"sendStart":0.368,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/bf5d7853585919974955302b636e8680d8cff37cd12c87b86bc882e4e60ebc67/original"},"timestamp":1925.988669,"type":"Image"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457190}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":13188,"encodedDataLength":0,"requestId":"9990.139","timestamp":1925.988724}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457190}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":13577,"requestId":"9990.139","timestamp":1925.985461}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457190}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1926.001263},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/2bc2051b1cd3b93471d477bed00a49cf09b9c8e11507f2a644fea5f3976808ea/original",":scheme":"https","accept":"*/*","accept-encoding":"identity;q=1, *;q=0","accept-language":"en-US,en;q=0.9","priority":"i","range":"bytes=0-","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"video","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.180","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457202}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":92879,"lineNumber":185,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Accept-Encoding":"identity;q=1, *;q=0","Range":"bytes=0-","Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/2bc2051b1cd3b93471d477bed00a49cf09b9c8e11507f2a644fea5f3976808ea/original"},"requestId":"9990.180","timestamp":1926.000744,"type":"Media","wallTime":1726547457.20051}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457202}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1926.003647},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/208c2dace3612eaeaf6790773b67fefecf9d35ef7f5326a2b7b2df5e0d72985e/original",":scheme":"https","accept":"*/*","accept-encoding":"identity;q=1, *;q=0","accept-language":"en-US,en;q=0.9","priority":"i","range":"bytes=0-","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"video","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.181","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457204}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":92879,"lineNumber":185,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Accept-Encoding":"identity;q=1, *;q=0","Range":"bytes=0-","Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/208c2dace3612eaeaf6790773b67fefecf9d35ef7f5326a2b7b2df5e0d72985e/original"},"requestId":"9990.181","timestamp":1926.001897,"type":"Media","wallTime":1726547457.202907}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457204}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":92879,"lineNumber":185,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Accept-Encoding":"identity;q=1, *;q=0","Range":"bytes=0-","Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/8084bbe655829745bd0153dd3ec12c90df92d48928277d0d66a99f84de920cdc/original"},"requestId":"9990.182","timestamp":1926.005291,"type":"Media","wallTime":1726547457.205031}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457207}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1926.005822},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/8084bbe655829745bd0153dd3ec12c90df92d48928277d0d66a99f84de920cdc/original",":scheme":"https","accept":"*/*","accept-encoding":"identity;q=1, *;q=0","accept-language":"en-US,en;q=0.9","priority":"i","range":"bytes=0-","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"video","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.182","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457207}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":92879,"lineNumber":185,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Accept-Encoding":"identity;q=1, *;q=0","Range":"bytes=0-","Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/ead2f6124dc302504220147274c2cd13aae821a63b91ca8a5bdacd80f5731e41/original"},"requestId":"9990.183","timestamp":1926.006756,"type":"Media","wallTime":1726547457.206482}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457208}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1926.007143},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/ead2f6124dc302504220147274c2cd13aae821a63b91ca8a5bdacd80f5731e41/original",":scheme":"https","accept":"*/*","accept-encoding":"identity;q=1, *;q=0","accept-language":"en-US,en;q=0.9","priority":"i","range":"bytes=0-","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"video","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.183","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457208}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"Content-Length":"403530","Content-Range":"bytes 0-403529/403530","accept-ranges":"bytes","age":"5478036","cache-control":"max-age=365000000, immutable","content-type":"video/mp4","date":"Mon, 15 Jul 2024 18:50:22 GMT","etag":"\\"5dca7b17e492904c552d81ed78521400\\"","last-modified":"Mon, 15 Jul 2024 18:19:29 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"GeFfDcgS1c2bfZOo8-N0fwfkJQSsdZuj7SH_7Rs8BgPnuyEl6yhLlA==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.180","resourceIPAddressSpace":"Public","statusCode":206}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457215}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"Content-Length":"492669","Content-Range":"bytes 0-492668/492669","accept-ranges":"bytes","age":"9458100","cache-control":"max-age=365000000, immutable","content-type":"video/mp4","date":"Thu, 30 May 2024 17:15:58 GMT","etag":"\\"d5abd0b1136ca94280355dae27299eaa\\"","last-modified":"Tue, 21 May 2024 19:47:17 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"Un8ww91UstAkHx79R2Eeu8d8QKIFWlDaWOXf0X3AlZoioriQ58_27g==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.181","resourceIPAddressSpace":"Public","statusCode":206}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457216}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.180","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":397,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"Content-Length":"403530","Content-Range":"bytes 0-403529/403530","accept-ranges":"bytes","age":"5478036","cache-control":"max-age=365000000, immutable","content-type":"video/mp4","date":"Mon, 15 Jul 2024 18:50:22 GMT","etag":"\\"5dca7b17e492904c552d81ed78521400\\"","last-modified":"Mon, 15 Jul 2024 18:19:29 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"GeFfDcgS1c2bfZOo8-N0fwfkJQSsdZuj7SH_7Rs8BgPnuyEl6yhLlA==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"video/mp4","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547457211267e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":206,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":10.595,"receiveHeadersStart":10.281,"requestTime":1926.001263,"sendEnd":0.601,"sendStart":0.389,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/2bc2051b1cd3b93471d477bed00a49cf09b9c8e11507f2a644fea5f3976808ea/original"},"timestamp":1926.019329,"type":"Media"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457221}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":403530,"encodedDataLength":0,"requestId":"9990.180","timestamp":1926.019932}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457221}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.181","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":398,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"Content-Length":"492669","Content-Range":"bytes 0-492668/492669","accept-ranges":"bytes","age":"9458100","cache-control":"max-age=365000000, immutable","content-type":"video/mp4","date":"Thu, 30 May 2024 17:15:58 GMT","etag":"\\"d5abd0b1136ca94280355dae27299eaa\\"","last-modified":"Tue, 21 May 2024 19:47:17 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"Un8ww91UstAkHx79R2Eeu8d8QKIFWlDaWOXf0X3AlZoioriQ58_27g==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"video/mp4","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547457213908e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":206,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":10.78,"receiveHeadersStart":10.544,"requestTime":1926.003647,"sendEnd":0.511,"sendStart":0.325,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/208c2dace3612eaeaf6790773b67fefecf9d35ef7f5326a2b7b2df5e0d72985e/original"},"timestamp":1926.020707,"type":"Media"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457225}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":196608,"encodedDataLength":0,"requestId":"9990.181","timestamp":1926.021142}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457225}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"access-control-allow-credentials":"true","access-control-allow-headers":"authorization,content-type,x-application-version,x-bamsdk-client-id,x-bamsdk-platform,x-bamsdk-platform-id,x-bamsdk-version,x-bamtech-wpnx-mlp-identifier,x-bamtech-wpnx-mlp-locale","access-control-allow-methods":"GET, POST, PUT, PATCH, DELETE, OPTIONS","access-control-allow-origin":"https://www.disneyplus.com","access-control-expose-headers":"x-request-id, x-bamtech-region, date","access-control-max-age":"600","cache-control":"public, max-age=3600","date":"Tue, 17 Sep 2024 04:30:57 GMT","vary":"origin,access-control-request-headers","via":"1.1 f877ee79a0f8fd4e0f5c08d722425c50.cloudfront.net (CloudFront)","x-amz-cf-id":"-ROWzgNrAqaHePAhzXVEB2QsXW3p8SpUjNTy79RCRNiRphRLOVKA3Q==","x-amz-cf-pop":"LAX50-C4","x-bamtech-region":"us-west-2","x-cache":"Miss from cloudfront","x-request-id":"5ad4cf716aa70342556985080fbd9759"},"requestId":"5D60B9F7D02C7B80F4BCAB8B8FF213BB","resourceIPAddressSpace":"Public","statusCode":204}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457225}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"Content-Length":"324625","Content-Range":"bytes 0-324624/324625","accept-ranges":"bytes","age":"9458100","cache-control":"max-age=365000000, immutable","content-type":"video/mp4","date":"Thu, 30 May 2024 17:15:58 GMT","etag":"\\"24f8faf195f90fccd6e138bcccaa549c\\"","last-modified":"Thu, 25 Apr 2024 20:20:45 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"hSLdqjFxoVYq2hjaJLwbwMQggvjGCEaQ_zRA0-gvTNKUWcgNJCzqow==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.182","resourceIPAddressSpace":"Public","statusCode":206}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457227}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"hasExtraInfo":true,"loaderId":"","requestId":"5D60B9F7D02C7B80F4BCAB8B8FF213BB","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":497,"connectionReused":false,"encodedDataLength":659,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"access-control-allow-credentials":"true","access-control-allow-headers":"authorization,content-type,x-application-version,x-bamsdk-client-id,x-bamsdk-platform,x-bamsdk-platform-id,x-bamsdk-version,x-bamtech-wpnx-mlp-identifier,x-bamtech-wpnx-mlp-locale","access-control-allow-methods":"GET, POST, PUT, PATCH, DELETE, OPTIONS","access-control-allow-origin":"https://www.disneyplus.com","access-control-expose-headers":"x-request-id, x-bamtech-region, date","access-control-max-age":"600","cache-control":"public, max-age=3600","date":"Tue, 17 Sep 2024 04:30:57 GMT","vary":"origin,access-control-request-headers","via":"1.1 f877ee79a0f8fd4e0f5c08d722425c50.cloudfront.net (CloudFront)","x-amz-cf-id":"-ROWzgNrAqaHePAhzXVEB2QsXW3p8SpUjNTy79RCRNiRphRLOVKA3Q==","x-amz-cf-pop":"LAX50-C4","x-bamtech-region":"us-west-2","x-cache":"Miss from cloudfront","x-request-id":"5ad4cf716aa70342556985080fbd9759"},"mimeType":"","protocol":"h2","remoteIPAddress":"54.230.21.87","remotePort":443,"responseTime":1.726547457224194e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M02","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.api.edge.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100C9D4C8B1D381FA5C970FEE11D6BAB54BD116C2B7B137987B3035952C12D2C5F0022100836D593EE526F607B3C0F6FE14F72993D83D55DED81000BCDD363B619BC59226","status":"Verified","timestamp":1.703699994992e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100912057400F49883625FFF9D3F09111E539EBC6FD1641CCB3D0D9CD5DD2498EA30220041A011CFE610C8A0FCFEC85C14BA593717BF8D363CE60917BCCE1B2F6592BE2","status":"Verified","timestamp":1.703699994987e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220172DF0F8673B45DE0BA4FDB23808A33451A46552900CD3DB9BE2AC27F457E430022100F241AAF8BD19DB50B6BD108D3110EA161CDCAAF6527F406D4FF83AD88CB890C3","status":"Verified","timestamp":1.70369999503e+12}],"subjectName":"*.api.edge.bamgrid.com","validFrom":1703635200,"validTo":1737676799},"securityState":"secure","status":204,"statusText":"","timing":{"connectEnd":91.593,"connectStart":62.366,"dnsEnd":62.184,"dnsStart":0.144,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":129.089,"receiveHeadersStart":128.94,"requestTime":1925.895526,"sendEnd":92,"sendStart":91.825,"sslEnd":91.583,"sslStart":74.638,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://disney.api.edge.bamgrid.com/graph/v1/device/graphql"},"timestamp":1926.02674,"type":"Preflight"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457227}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":0,"requestId":"5D60B9F7D02C7B80F4BCAB8B8FF213BB","timestamp":1926.026419}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457227}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1926.028239},"headers":{":authority":"disney.api.edge.bamgrid.com",":method":"POST",":path":"/graph/v1/device/graphql",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","authorization":"Bearer ZGlzbmV5JmJyb3dzZXImMS4wLjA.Cu56AgSfBTDag5NiRA81oLHkDZfu5L3CKadnefEAY84","content-length":"755","content-type":"application/json","origin":"https://www.disneyplus.com","priority":"u=1, i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"empty","sec-fetch-mode":"cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","x-application-version":"b928d05b","x-bamsdk-client-id":"disney-svod-3d9324fc","x-bamsdk-platform":"javascript/linux}/chrome","x-bamsdk-platform-id":"browser","x-bamsdk-version":"b928d05b-dplus-mlp","x-bamtech-wpnx-mlp-identifier":"/","x-bamtech-wpnx-mlp-locale":"en-us"},"requestId":"9990.103","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457229}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"Content-Length":"357966","Content-Range":"bytes 0-357965/357966","accept-ranges":"bytes","age":"9458100","cache-control":"max-age=365000000, immutable","content-type":"video/mp4","date":"Thu, 30 May 2024 17:15:58 GMT","etag":"\\"1e564107442964d7c05b164e3d103860\\"","last-modified":"Thu, 25 Apr 2024 21:11:00 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"1dBCVpXqoYcsSx7GqYOCjF0rWAe6pTIIkEByDXKXcXfIXf90xi--WA==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.183","resourceIPAddressSpace":"Public","statusCode":206}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457231}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.182","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":399,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"Content-Length":"324625","Content-Range":"bytes 0-324624/324625","accept-ranges":"bytes","age":"9458100","cache-control":"max-age=365000000, immutable","content-type":"video/mp4","date":"Thu, 30 May 2024 17:15:58 GMT","etag":"\\"24f8faf195f90fccd6e138bcccaa549c\\"","last-modified":"Thu, 25 Apr 2024 20:20:45 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"hSLdqjFxoVYq2hjaJLwbwMQggvjGCEaQ_zRA0-gvTNKUWcgNJCzqow==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"video/mp4","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547457225066e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":206,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":19.743,"receiveHeadersStart":19.526,"requestTime":1926.005822,"sendEnd":0.479,"sendStart":0.326,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/8084bbe655829745bd0153dd3ec12c90df92d48928277d0d66a99f84de920cdc/original"},"timestamp":1926.031403,"type":"Media"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457232}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":131072,"encodedDataLength":0,"requestId":"9990.182","timestamp":1926.032126}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457232}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.183","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":400,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"Content-Length":"357966","Content-Range":"bytes 0-357965/357966","accept-ranges":"bytes","age":"9458100","cache-control":"max-age=365000000, immutable","content-type":"video/mp4","date":"Thu, 30 May 2024 17:15:58 GMT","etag":"\\"1e564107442964d7c05b164e3d103860\\"","last-modified":"Thu, 25 Apr 2024 21:11:00 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"1dBCVpXqoYcsSx7GqYOCjF0rWAe6pTIIkEByDXKXcXfIXf90xi--WA==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"video/mp4","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.72654745723083e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":206,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":24.184,"receiveHeadersStart":23.955,"requestTime":1926.007143,"sendEnd":0.397,"sendStart":0.265,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/ead2f6124dc302504220147274c2cd13aae821a63b91ca8a5bdacd80f5731e41/original"},"timestamp":1926.035075,"type":"Media"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457236}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":65536,"encodedDataLength":245524,"requestId":"9990.183","timestamp":1926.037179}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457237}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":25972,"lineNumber":211,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Accept-Encoding":"identity;q=1, *;q=0","Range":"bytes=0-","Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/7c50a1bbb85b95289b6250bcaccfbc84c138a13e445ce5a927573e424573c1b5/original"},"requestId":"9990.187","timestamp":1926.041806,"type":"Media","wallTime":1726547457.241559}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457242}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1926.042426},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/7c50a1bbb85b95289b6250bcaccfbc84c138a13e445ce5a927573e424573c1b5/original",":scheme":"https","accept":"*/*","accept-encoding":"identity;q=1, *;q=0","accept-language":"en-US,en;q=0.9","priority":"i","range":"bytes=0-","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"video","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.187","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457243}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"columnNumber":25972,"lineNumber":211,"type":"parser","url":"https://www.disneyplus.com/"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Accept-Encoding":"identity;q=1, *;q=0","Range":"bytes=0-","Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://cnbl-cdn.bamgrid.com/assets/76ee6218d77092515eb6fe39345ba49962a0779b36f9fe71a63992c016649554/original"},"requestId":"9990.188","timestamp":1926.044871,"type":"Media","wallTime":1726547457.244717}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457246}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1926.045433},"headers":{":authority":"cnbl-cdn.bamgrid.com",":method":"GET",":path":"/assets/76ee6218d77092515eb6fe39345ba49962a0779b36f9fe71a63992c016649554/original",":scheme":"https","accept":"*/*","accept-encoding":"identity;q=1, *;q=0","accept-language":"en-US,en;q=0.9","priority":"i","range":"bytes=0-","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"video","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.188","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457246}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"Content-Length":"387144","Content-Range":"bytes 0-387143/387144","accept-ranges":"bytes","age":"9458100","cache-control":"max-age=365000000, immutable","content-type":"video/mp4","date":"Thu, 30 May 2024 17:15:58 GMT","etag":"\\"2ac074bc0348aafe017205b55e79d0c5\\"","last-modified":"Tue, 14 May 2024 16:38:24 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"34BTE8bb-BCgMrII--EVAR03zKfLUxNXvu8PLUl6uRU9js18YXQfOA==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.187","resourceIPAddressSpace":"Public","statusCode":206}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457255}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"Content-Length":"346745","Content-Range":"bytes 0-346744/346745","accept-ranges":"bytes","age":"9458100","cache-control":"max-age=365000000, immutable","content-type":"video/mp4","date":"Thu, 30 May 2024 17:15:58 GMT","etag":"\\"11c7986d0ac8b323be111ec5db633425\\"","last-modified":"Thu, 25 Apr 2024 20:20:45 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"G6YLsFx2TcDHVCaR_UJU2vhp8xB7BBUcTyU9EeyTiKm3wnEbEDFLBQ==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"requestId":"9990.188","resourceIPAddressSpace":"Public","statusCode":206}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457256}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"stack":{"callFrames":[{"columnNumber":345,"functionName":"","lineNumber":0,"scriptId":"37","url":"https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/oneTrustConsentBundle.90d4ea260c.js"}]},"type":"script"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Low","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://geolocation.onetrust.com/cookieconsentpub/v1/geo/countrycode"},"requestId":"9990.196","timestamp":1926.05211,"type":"Script","wallTime":1726547457.25202}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457260}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.187","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":400,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"Content-Length":"387144","Content-Range":"bytes 0-387143/387144","accept-ranges":"bytes","age":"9458100","cache-control":"max-age=365000000, immutable","content-type":"video/mp4","date":"Thu, 30 May 2024 17:15:58 GMT","etag":"\\"2ac074bc0348aafe017205b55e79d0c5\\"","last-modified":"Tue, 14 May 2024 16:38:24 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"34BTE8bb-BCgMrII--EVAR03zKfLUxNXvu8PLUl6uRU9js18YXQfOA==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"video/mp4","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547457253156e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":206,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":11.254,"receiveHeadersStart":11.007,"requestTime":1926.042426,"sendEnd":0.763,"sendStart":0.483,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/7c50a1bbb85b95289b6250bcaccfbc84c138a13e445ce5a927573e424573c1b5/original"},"timestamp":1926.061245,"type":"Media"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457265}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":387144,"encodedDataLength":0,"requestId":"9990.187","timestamp":1926.061753}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457266}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.188","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":123,"connectionReused":true,"encodedDataLength":400,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"Content-Length":"346745","Content-Range":"bytes 0-346744/346745","accept-ranges":"bytes","age":"9458100","cache-control":"max-age=365000000, immutable","content-type":"video/mp4","date":"Thu, 30 May 2024 17:15:58 GMT","etag":"\\"11c7986d0ac8b323be111ec5db633425\\"","last-modified":"Thu, 25 Apr 2024 20:20:45 GMT","server":"AmazonS3","via":"1.1 cae250e28586d12c16dcc4b462ac538c.cloudfront.net (CloudFront)","x-amz-cf-id":"G6YLsFx2TcDHVCaR_UJU2vhp8xB7BBUcTyU9EeyTiKm3wnEbEDFLBQ==","x-amz-cf-pop":"PHX52-P1","x-amz-server-side-encryption":"AES256","x-cache":"Hit from cloudfront"},"mimeType":"video/mp4","protocol":"h2","remoteIPAddress":"18.238.85.127","remotePort":443,"responseTime":1.726547457255423e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h2\' log","logId":"12F14E34BD53724C840619C38F3F7A13F8E7B56287889C6D300584EBE586263A","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100A8FA7F4A91AB80583B4148A9E581B5E4DE49268BC95473B1F225D8C766030DA302207A9830B1BBC11D37785660DF4F08EF7D5769FF84C4B71CC0DBB154329EC3F3BD","status":"Verified","timestamp":1.719317333629e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100DC60F74C5450F9D9CE9356C43A52C8A532EE30382B737F56920A7B72EDAE40A202201AB2052347E40481877765921EE8786FC83DE4515CCC9B59F8B5ADA95B3BE4CA","status":"Verified","timestamp":1.719317333619e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220342BC9A6FE577AB71B21EBF191AE70C8EDF364B9A8DDA80BA12B300B52B1CD6F022100CDB12C15AB8CB85A14B2CC5F50AC9F9D103F2399D3743728B5C368C20AA14C97","status":"Verified","timestamp":1.71931733364e+12}],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":206,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":10.499,"receiveHeadersStart":10.271,"requestTime":1926.045433,"sendEnd":0.667,"sendStart":0.458,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://cnbl-cdn.bamgrid.com/assets/76ee6218d77092515eb6fe39345ba49962a0779b36f9fe71a63992c016649554/original"},"timestamp":1926.063894,"type":"Media"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457266}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":346745,"encodedDataLength":0,"requestId":"9990.188","timestamp":1926.064342}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457266}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":411229,"encodedDataLength":316414,"requestId":"9990.75","timestamp":1926.068244}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457269}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.180","timestamp":1926.084704,"type":"Media"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457284}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1926.052824},"headers":{":authority":"geolocation.onetrust.com",":method":"GET",":path":"/cookieconsentpub/v1/geo/countrycode",":scheme":"https","accept":"*/*","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"script","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.196","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457299}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"access-control-allow-credentials":"true","access-control-allow-methods":"GET, POST, PUT, PATCH, DELETE, OPTIONS","access-control-allow-origin":"https://www.disneyplus.com","access-control-expose-headers":"x-request-id, x-bamtech-region, date","access-control-max-age":"600","cache-control":"no-store","content-encoding":"gzip","content-type":"application/json","date":"Tue, 17 Sep 2024 04:30:57 GMT","vary":"origin, access-control-request-headers","via":"1.1 f877ee79a0f8fd4e0f5c08d722425c50.cloudfront.net (CloudFront)","x-amz-cf-id":"L9_hIWhqTfMCNtnCBp9oeTdlC_27BM1S1Jlh6uie-EAoeAwFHJL8qQ==","x-amz-cf-pop":"LAX50-C4","x-bamtech-region":"us-west-2","x-cache":"Miss from cloudfront","x-request-id":"0b23d39fcf0fa7d6252d04f6cb4bc642"},"requestId":"9990.103","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457305}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.103","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":497,"connectionReused":true,"encodedDataLength":523,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"access-control-allow-credentials":"true","access-control-allow-methods":"GET, POST, PUT, PATCH, DELETE, OPTIONS","access-control-allow-origin":"https://www.disneyplus.com","access-control-expose-headers":"x-request-id, x-bamtech-region, date","access-control-max-age":"600","cache-control":"no-store","content-encoding":"gzip","content-type":"application/json","date":"Tue, 17 Sep 2024 04:30:57 GMT","vary":"origin, access-control-request-headers","via":"1.1 f877ee79a0f8fd4e0f5c08d722425c50.cloudfront.net (CloudFront)","x-amz-cf-id":"L9_hIWhqTfMCNtnCBp9oeTdlC_27BM1S1Jlh6uie-EAoeAwFHJL8qQ==","x-amz-cf-pop":"LAX50-C4","x-bamtech-region":"us-west-2","x-cache":"Miss from cloudfront","x-request-id":"0b23d39fcf0fa7d6252d04f6cb4bc642"},"mimeType":"application/json","protocol":"h2","remoteIPAddress":"54.230.21.87","remotePort":443,"responseTime":1.726547457305043e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M02","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.api.edge.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2025h1\' log","logId":"4E75A3275C9A10C3385B6CD4DF3F52EB1DF0E08E1B8D69C0B1FA64B1629A39DF","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100C9D4C8B1D381FA5C970FEE11D6BAB54BD116C2B7B137987B3035952C12D2C5F0022100836D593EE526F607B3C0F6FE14F72993D83D55DED81000BCDD363B619BC59226","status":"Verified","timestamp":1.703699994992e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Yeti2025 Log","logId":"7D591E12E1782A7B1C61677C5EFDF8D0875C14A04E959EB9032FD90E8C2E79B8","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3045022100912057400F49883625FFF9D3F09111E539EBC6FD1641CCB3D0D9CD5DD2498EA30220041A011CFE610C8A0FCFEC85C14BA593717BF8D363CE60917BCCE1B2F6592BE2","status":"Verified","timestamp":1.703699994987e+12},{"hashAlgorithm":"SHA-256","logDescription":"DigiCert Nessie2025 Log","logId":"E6D2316340778CC1104106D771B9CEC1D240F6968486FBBA87321DFD1E378E50","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"30450220172DF0F8673B45DE0BA4FDB23808A33451A46552900CD3DB9BE2AC27F457E430022100F241AAF8BD19DB50B6BD108D3110EA161CDCAAF6527F406D4FF83AD88CB890C3","status":"Verified","timestamp":1.70369999503e+12}],"subjectName":"*.api.edge.bamgrid.com","validFrom":1703635200,"validTo":1737676799},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":77.252,"receiveHeadersStart":77.058,"requestTime":1926.028239,"sendEnd":1.739,"sendStart":0.838,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://disney.api.edge.bamgrid.com/graph/v1/device/graphql"},"timestamp":1926.106649,"type":"Fetch"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457311}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":533,"encodedDataLength":333,"requestId":"9990.103","timestamp":1926.113833}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457315}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":856,"requestId":"9990.103","timestamp":1926.106613}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457315}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":193553,"encodedDataLength":0,"requestId":"9990.182","timestamp":1926.116807}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457316}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":292430,"encodedDataLength":0,"requestId":"9990.183","timestamp":1926.122088}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457323}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.181","timestamp":1926.122746,"type":"Media"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457323}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"cf-ray":"8c465d282a5a7ed1-LAX","content-length":"27","content-type":"text/javascript","date":"Tue, 17 Sep 2024 04:30:57 GMT","server":"cloudflare","strict-transport-security":"max-age=31536000; includeSubDomains; preload","vary":"Accept-Encoding"},"requestId":"9990.196","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457328}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.182","timestamp":1926.130397,"type":"Media"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457330}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":true,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.196","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":560,"connectionReused":false,"encodedDataLength":133,"fromDiskCache":false,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"cf-ray":"8c465d282a5a7ed1-LAX","content-length":"27","content-type":"text/javascript","date":"Tue, 17 Sep 2024 04:30:57 GMT","server":"cloudflare","strict-transport-security":"max-age=31536000; includeSubDomains; preload","vary":"Accept-Encoding"},"mimeType":"text/javascript","protocol":"h2","remoteIPAddress":"172.64.155.119","remotePort":443,"responseTime":1.726547457328261e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"compliant","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"WE1","keyExchange":"","keyExchangeGroup":"X25519Kyber768Draft00","protocol":"TLS 1.3","sanList":["geolocation.onetrust.com"],"serverSignatureAlgorithm":1027,"signedCertificateTimestampList":[{"hashAlgorithm":"SHA-256","logDescription":"Google \'Argon2024\' log","logId":"EECDD064D5DB1ACEC55CB79DB4CD13A23287467CBCECDEC351485946711FB59B","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"304502205ECC7A262E2204E0847BB5C1395B02B8A28E6A3FA575D057E508657257733DFA022100B9D6E780EA2250E9C37B154BD7E925E32669186F0433463E070493CFBC6AB757","status":"Verified","timestamp":1.723577226653e+12},{"hashAlgorithm":"SHA-256","logDescription":"Let\'s Encrypt \'Oak2024H2\' log","logId":"3F174B4FD7224758941D651C84BE0D12ED90377F1F856AEBC1BF2885ECF8646E","origin":"Embedded in certificate","signatureAlgorithm":"ECDSA","signatureData":"3046022100B5F86D6B23BFA1F365C09B05B6F51083AD3E1DA0F3818DE1AB9457A0FDFE24D5022100C78AC2D27395B22EB6862A5D6990341C0D43658BAF9BB17F913485D8621564B5","status":"Verified","timestamp":1.723577226667e+12}],"subjectName":"geolocation.onetrust.com","validFrom":1723573626,"validTo":1731353222},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":46.096,"connectStart":14.069,"dnsEnd":13.939,"dnsStart":0.259,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":75.878,"receiveHeadersStart":75.719,"requestTime":1926.052824,"sendEnd":46.519,"sendStart":46.36,"sslEnd":46.085,"sslStart":24.976,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://geolocation.onetrust.com/cookieconsentpub/v1/geo/countrycode"},"timestamp":1926.143862,"type":"Script"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457344}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":27,"encodedDataLength":0,"requestId":"9990.196","timestamp":1926.143934}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457344}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":316882,"requestId":"9990.75","timestamp":1925.936921}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457345}
{'level': 'INFO', 'message': '{"message":{"method":"Page.domContentEventFired","params":{"timestamp":1926.384765}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457594}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.188","timestamp":1926.388914,"type":"Media"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457594}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":178,"requestId":"9990.196","timestamp":1926.129523}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457594}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.187","timestamp":1926.392799,"type":"Media"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457595}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFailed","params":{"canceled":true,"errorText":"net::ERR_ABORTED","requestId":"9990.183","timestamp":1926.393484,"type":"Media"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457595}
{'level': 'INFO', 'message': '{"message":{"method":"Page.loadEventFired","params":{"timestamp":1926.396606}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457597}
{'level': 'INFO', 'message': '{"message":{"method":"Page.frameStoppedLoading","params":{"frameId":"3E7284AA00690624BB019FC4430314BC"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457598}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"type":"other"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"Medium","isSameSite":true,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://www.disneyplus.com/manifest.json"},"requestId":"9990.197","timestamp":1926.399424,"type":"Manifest","wallTime":1726547457.599162}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457601}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSentExtraInfo","params":{"associatedCookies":[],"clientSecurityState":{"initiatorIPAddressSpace":"Public","initiatorIsSecureContext":true,"privateNetworkRequestPolicy":"PreflightWarn"},"connectTiming":{"requestTime":1926.400949},"headers":{":authority":"static-assets.bamgrid.com",":method":"GET",":path":"/product/disneyplus/favicons/favicon_dis_48x48_@2X.2eebc912779d4f2ee8d9c6204d443ab6.png",":scheme":"https","accept":"image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8","accept-encoding":"gzip, deflate, br, zstd","accept-language":"en-US,en;q=0.9","priority":"u=1, i","referer":"https://www.disneyplus.com/","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\"","sec-fetch-dest":"image","sec-fetch-mode":"no-cors","sec-fetch-site":"cross-site","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36"},"requestId":"9990.198","siteHasCookieInOtherPartition":false}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457602}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"type":"other"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"High","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://static-assets.bamgrid.com/product/disneyplus/favicons/favicon_dis_48x48_@2X.2eebc912779d4f2ee8d9c6204d443ab6.png"},"requestId":"9990.198","timestamp":1926.400581,"type":"Other","wallTime":1726547457.60031}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457602}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":false,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.197","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":0,"connectionReused":false,"encodedDataLength":0,"fromDiskCache":true,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"Access-Control-Allow-Methods":"HEAD, GET","Access-Control-Allow-Origin":"*","Access-Control-Max-Age":"3000","Cache-Control":"max-age=34","Content-Encoding":"gzip","Content-Length":"449","Content-Type":"application/json","Date":"Tue, 17 Sep 2024 04:30:56 GMT","ETag":"W/\\"79399f9bae72975dad01ed3c5fdf111c\\"","Last-Modified":"Thu, 22 Aug 2024 18:55:38 GMT","Server":"AmazonS3","Timing-Allow-Origin":"*","Vary":"Accept-Encoding","X-Amz-Cf-Id":"K0l088iRM3oqi_4RmVr5C-0UnllzbCNyvw9XR0hgJ2ojr2i9xp-uHA==","X-Amz-Cf-Pop":"LAX50-C3","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":".IiqWQGsKEORzPKlyxGhTM.64LsyvIK7"},"mimeType":"application/json","protocol":"http/1.1","remoteIPAddress":"23.44.150.44","remotePort":443,"responseTime":1.726547456569791e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"unknown","cipher":"AES_256_GCM","encryptedClientHello":false,"issuer":"COMODO RSA Organization Validation Secure Server CA","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.disneyplus.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[],"subjectName":"*.disneyplus.com","validFrom":1705968000,"validTo":1737590399},"securityState":"secure","status":200,"statusText":"OK","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":1.726,"receiveHeadersStart":1.647,"requestTime":1926.399885,"sendEnd":0.106,"sendStart":0.106,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://www.disneyplus.com/manifest.json"},"timestamp":1926.403231,"type":"Manifest"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457605}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":1139,"encodedDataLength":0,"requestId":"9990.197","timestamp":1926.403392}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457605}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":0,"requestId":"9990.197","timestamp":1926.4027}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457605}
{'level': 'INFO', 'message': '{"message":{"method":"Network.requestWillBeSent","params":{"documentURL":"https://www.disneyplus.com/","frameId":"3E7284AA00690624BB019FC4430314BC","hasUserGesture":false,"initiator":{"type":"other"},"loaderId":"939C9171ED8FE2B6C35C286E1883435F","redirectHasExtraInfo":false,"request":{"headers":{"Referer":"https://www.disneyplus.com/","User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/128.0.0.0 Safari/537.36","sec-ch-ua":"\\"Chromium\\";v=\\"128\\", \\"Not;A=Brand\\";v=\\"24\\", \\"Google Chrome\\";v=\\"128\\"","sec-ch-ua-mobile":"?0","sec-ch-ua-platform":"\\"Linux\\""},"initialPriority":"High","isSameSite":false,"method":"GET","mixedContentType":"none","referrerPolicy":"strict-origin-when-cross-origin","url":"https://static-assets.bamgrid.com/product/disneyplus/favicons/msftpwa-192x192-aurora.97f08a1eb58995c81687d0cf3f953796.png"},"requestId":"9990.199","timestamp":1926.405554,"type":"Other","wallTime":1726547457.605285}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457606}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceivedExtraInfo","params":{"blockedCookies":[],"cookiePartitionKey":{"hasCrossSiteAncestor":true,"topLevelSite":"https://disneyplus.com"},"cookiePartitionKeyOpaque":false,"exemptedCookies":[],"headers":{"accept-ranges":"bytes","age":"101","cache-control":"max-age=300","content-length":"2841","content-type":"image/png","date":"Tue, 17 Sep 2024 04:29:17 GMT","etag":"\\"2eebc912779d4f2ee8d9c6204d443ab6\\"","last-modified":"Wed, 28 Aug 2024 21:28:06 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 db760bd4935f16e1b5c20ab5690be478.cloudfront.net (CloudFront)","x-amz-cf-id":"ZK15vYkMiIX6xytInQ8GKexcZMuSOTcn2Fq4RRTd0Pog-277ndhfMg==","x-amz-cf-pop":"LAX54-P2","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"XMkgB4bwo8VtJy9jjrvG2AQTEAbgENty","x-cache":"Hit from cloudfront"},"requestId":"9990.198","resourceIPAddressSpace":"Public","statusCode":200}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457612}
{'level': 'INFO', 'message': '{"message":{"method":"Network.responseReceived","params":{"frameId":"3E7284AA00690624BB019FC4430314BC","hasExtraInfo":false,"loaderId":"939C9171ED8FE2B6C35C286E1883435F","requestId":"9990.199","response":{"alternateProtocolUsage":"unspecifiedReason","charset":"","connectionId":0,"connectionReused":false,"encodedDataLength":0,"fromDiskCache":true,"fromPrefetchCache":false,"fromServiceWorker":false,"headers":{"accept-ranges":"bytes","age":"62","cache-control":"max-age=300","content-length":"46114","content-type":"image/png","date":"Tue, 17 Sep 2024 04:29:55 GMT","etag":"\\"97f08a1eb58995c81687d0cf3f953796\\"","last-modified":"Wed, 28 Aug 2024 21:28:06 GMT","server":"AmazonS3","timing-allow-origin":"*","vary":"Accept-Encoding","via":"1.1 db760bd4935f16e1b5c20ab5690be478.cloudfront.net (CloudFront)","x-amz-cf-id":"afTNPop0cqNwm0RYZniKoSDaMmZ7ey_klI7bM052PEVRjHfepq4AFA==","x-amz-cf-pop":"LAX54-P2","x-amz-replication-status":"COMPLETED","x-amz-server-side-encryption":"AES256","x-amz-version-id":"C_wyL.fslbZiYCtHWIt3D7ob5c0.C3Mz","x-cache":"Hit from cloudfront"},"mimeType":"image/png","protocol":"h2","remoteIPAddress":"3.168.132.100","remotePort":443,"responseTime":1.726547456601479e+12,"securityDetails":{"certificateId":0,"certificateTransparencyCompliance":"unknown","cipher":"AES_128_GCM","encryptedClientHello":false,"issuer":"Amazon RSA 2048 M03","keyExchange":"","keyExchangeGroup":"X25519","protocol":"TLS 1.3","sanList":["*.bamgrid.com"],"serverSignatureAlgorithm":2052,"signedCertificateTimestampList":[],"subjectName":"*.bamgrid.com","validFrom":1719273600,"validTo":1753315199},"securityState":"secure","status":200,"statusText":"","timing":{"connectEnd":-1,"connectStart":-1,"dnsEnd":-1,"dnsStart":-1,"proxyEnd":-1,"proxyStart":-1,"pushEnd":0,"pushStart":0,"receiveHeadersEnd":1.015,"receiveHeadersStart":0.947,"requestTime":1926.405958,"sendEnd":0.248,"sendStart":0.248,"sslEnd":-1,"sslStart":-1,"workerFetchStart":-1,"workerReady":-1,"workerRespondWithSettled":-1,"workerStart":-1},"url":"https://static-assets.bamgrid.com/product/disneyplus/favicons/msftpwa-192x192-aurora.97f08a1eb58995c81687d0cf3f953796.png"},"timestamp":1926.408407,"type":"Other"}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457613}
{'level': 'INFO', 'message': '{"message":{"method":"Network.dataReceived","params":{"dataLength":46114,"encodedDataLength":0,"requestId":"9990.199","timestamp":1926.408641}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457613}
{'level': 'INFO', 'message': '{"message":{"method":"Network.loadingFinished","params":{"encodedDataLength":0,"requestId":"9990.199","timestamp":1926.407736}},"webview":"3E7284AA00690624BB019FC4430314BC"}', 'timestamp': 1726547457613}  
```
</details>

只打印网络 ：
```python
import json
from selenium import webdriver
import google_colab_selenium as gs

# 函数来处理浏览器日志条目
def process_browser_log_entry(entry):
    try:
        response = json.loads(entry['message'])['message']
        return response
    except json.JSONDecodeError:
        # 如果条目不是有效的JSON，则忽略它
        return None

# 设置Chrome选项以启用性能日志
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--enable-logging")
chrome_options.add_argument("--log-level=0")
chrome_options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

# 初始化WebDriver
driver = webdriver.Chrome(options=chrome_options)

# 打开网页
driver.get("https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ")

# 等待页面加载，这里我们简单地等待了10秒
driver.implicitly_wait(10)

# 获取性能日志
netLog = driver.get_log("performance")

# 处理日志条目并筛选出网络响应事件
events = [process_browser_log_entry(entry) for entry in netLog]
events = [event for event in events if event and 'Network.response' in event['method']]

# 初始化URL列表
detected_url = []

# 遍历事件并收集URL
for item in events:
    if "response" in item["params"]:
        if "url" in item["params"]["response"]:
            detected_url.append(item["params"]["response"]["url"])

# 打印收集到的URL
for url in detected_url:
    print(url)

# 停止WebDriver
driver.quit()
```

<details>
<summary>查看响应示例：</summary>
  
```
Updated and upgraded APT
Downloaded Google Chrome
Initialized Chromedriver
https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ
https://cnbl-cdn.bamgrid.com/assets/ae212c3972ec736bb5793a448280055f9e5921211d4ec316e5e2a472fc797949/original
https://static-assets.bamgrid.com/fonts/inspire/Inspire-Regular.f2199f841165c4ddbafcf177da3ef974.woff2
https://static-assets.bamgrid.com/fonts/inspire/Inspire-Bold.4ff15ddc93445342649194969715b0b5.woff2
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/css/d7217ef32a15aede.css
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/css/b503c746db7a0c4d.css
https://www.disneyplus.com/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ
https://static-assets.bamgrid.com/fonts/inspire/Inspire-Regular.f2199f841165c4ddbafcf177da3ef974.woff2
https://static-assets.bamgrid.com/fonts/inspire/Inspire-Bold.4ff15ddc93445342649194969715b0b5.woff2
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/css/d7217ef32a15aede.css
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/css/b503c746db7a0c4d.css
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/webpack-7eb13b5b99357ccb.js
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/framework-7ca4c7590a188064.js
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/main-deda6e05560430d9.js
https://www.disneyplus.com/manifest.json
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/pages/_app-04a807cd96ff1485.js
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/689-1704811563a7aad2.js
https://static-assets.bamgrid.com/product/disneyplus/favicons/msftpwa-192x192-aurora.97f08a1eb58995c81687d0cf3f953796.png
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/646-9fd3676fcc0efa42.js
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/182-74c9963345086f4c.js
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/292-02db2ad1e62c2a58.js
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/928-a3fb44f500ddd597.js
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/440-afce561b152fc100.js
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/chunks/pages/series/%5BprettyTitle%5D/%5Bslug%5D-b604066ab3641502.js
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/U6_u41-7WVYTgYdDlkjYi/_buildManifest.js
https://prod-static.disney-plus.net/us-east-1/disneyPlus/marketing-unified/_next/static/U6_u41-7WVYTgYdDlkjYi/_ssgManifest.js
https://www.disneyplus.com/
https://static-assets.bamgrid.com/fonts/inspire/Inspire-Regular.f2199f841165c4ddbafcf177da3ef974.woff2
https://static-assets.bamgrid.com/fonts/inspire/Inspire-Bold.4ff15ddc93445342649194969715b0b5.woff2
https://cnbl-cdn.bamgrid.com/assets/c599c52da8a32c4af829f672a5b040946ac2d49b41b018eebd86a09a21f44d2a/original
https://cnbl-cdn.bamgrid.com/assets/e7398ed4ffc16eb4eca63f549664da62cda5e6c172d799d7619f9609eac3df71/original
https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/styles/960.f3b881decbe333dfe114.css
https://cnbl-cdn.bamgrid.com/assets/6decfd2b11e14b849b0b0cbfce963b36a13dac47c7cff42600eea6043559d32a/original
https://www.datadoghq-browser-agent.com/us1/v4/datadog-rum.js
https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/oneTrustConsentBundle.90d4ea260c.js
https://cnbl-cdn.bamgrid.com/assets/5bc7286c5388eb678e209a579530895488b16071b25e7e4956e9526b00210f2e/original
https://cnbl-cdn.bamgrid.com/assets/e4202f3ff6aabf3aff8904cb75dcf97ab17ebc74d3b6d7c7d1498748f587f3b1/original
https://cnbl-cdn.bamgrid.com/assets/fa28d30b1356ba01fe9b34c9128757a3ac9889351f4dcd0851cf61cd6e8f9b8c/original
https://cnbl-cdn.bamgrid.com/assets/af368171ec6cc1872094a805cbaf20999a9bb7ea7abed1d04d02d6741001c308/original
https://cnbl-cdn.bamgrid.com/assets/2c13a1c721d0c05a8fe6b5f0607db70bf684da21657db25503ec8ae600f03672/original
https://cnbl-cdn.bamgrid.com/assets/01274f10c21df19cef0b42b85c547afbdf4901977ce9d46f7b06c48c5c987be6/original
https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/322.ace0d787afec5225e11a.js
https://cnbl-cdn.bamgrid.com/assets/bf5d7853585919974955302b636e8680d8cff37cd12c87b86bc882e4e60ebc67/original
https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/960.0a18b56674d234b108cb.js
https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/218.4d1210286d593d83228d.js
https://prod-static.disney-plus.net/us-east-1/disneyPlus/app/build/generic/scripts/marketing_script_bundle_v2.aa2876f89c04cbfdc1fe.js
https://disney.api.edge.bamgrid.com/graph/v1/device/graphql
https://cnbl-cdn.bamgrid.com/assets/2bc2051b1cd3b93471d477bed00a49cf09b9c8e11507f2a644fea5f3976808ea/original
https://cnbl-cdn.bamgrid.com/assets/208c2dace3612eaeaf6790773b67fefecf9d35ef7f5326a2b7b2df5e0d72985e/original
https://cnbl-cdn.bamgrid.com/assets/8084bbe655829745bd0153dd3ec12c90df92d48928277d0d66a99f84de920cdc/original
https://disney.api.edge.bamgrid.com/graph/v1/device/graphql
https://cnbl-cdn.bamgrid.com/assets/ead2f6124dc302504220147274c2cd13aae821a63b91ca8a5bdacd80f5731e41/original
https://cnbl-cdn.bamgrid.com/assets/7c50a1bbb85b95289b6250bcaccfbc84c138a13e445ce5a927573e424573c1b5/original
https://cnbl-cdn.bamgrid.com/assets/76ee6218d77092515eb6fe39345ba49962a0779b36f9fe71a63992c016649554/original
https://geolocation.onetrust.com/cookieconsentpub/v1/geo/countrycode
https://www.disneyplus.com/manifest.json  
```
</details>

参考  

qiita.com › [Python+Seleniumで Chromeデベロッパーツールの Networkタブ](https://qiita.com/nextpenguin/items/4827fb1da062581518e7)

获取图片 ：
`https://www.disneyplus.com/zh-hans/series/big-mouth/7kIy3S1m2HNY`对应
`https://content.global.edge.bamgrid.com/svc/content/DmcSeriesBundle/version/3.3/region/GB/audience/false/maturity/1450/language/en-GB/encodedSeriesId/3RUQKboZV3FF`

注意region/GB 的地区GB需要改，比如对于
 https://www.disneyplus.com/en-jp/series/frieren-beyond-journeys-end/1rlaH8IM0pkQ 就是 JP，这些链接直接在浏览器搜到

```
!apt install jq

!curl https://disney.content.edge.bamgrid.com/svc/content/DmcSeriesBundle/version/5.1/region/JP/audience/false/maturity/1850/language/zh-Hans/encodedSeriesId/1rlaH8IM0pkQ | jq
```
<details>
<summary>查看响应示例：</summary>
  
```
"流式输出内容被截断，只能显示最后 5000 行内容。
                },
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "1129698D299F194FED20FEDC826413E9F0FA5281613BC57E7E645B359B3D56C7",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/1129698D299F194FED20FEDC826413E9F0FA5281613BC57E7E645B359B3D56C7"
                    }
                  }
                },
                "1.33": {
                  "series": {
                    "default": {
                      "masterId": "9F23483E3484C1BF8A4641819F2B18A657747B64A2B4BD7414287B11D0386B99",
                      "masterWidth": 2880,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/9F23483E3484C1BF8A4641819F2B18A657747B64A2B4BD7414287B11D0386B99"
                    }
                  }
                }
              },
              "thumbnail": {
                "1.78": {
                  "program": {
                    "default": {
                      "masterId": "FFDADC5DA066BE87668321A54551E94B3FAB3CBD0B97C6993208E5CB65E2EFE0",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/FFDADC5DA066BE87668321A54551E94B3FAB3CBD0B97C6993208E5CB65E2EFE0"
                    }
                  }
                }
              },
              "background_up_next": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "0A0DA7884203201B1A13F29F8A52CCF4059F5E1377A10A0DF79951A3BF5F6B2C",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/0A0DA7884203201B1A13F29F8A52CCF4059F5E1377A10A0DF79951A3BF5F6B2C"
                    }
                  }
                }
              },
              "title_treatment_centered": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "56A9C8DA09747B319C6C419244665A8828C3F59B3469DD98261F9079B8D90360",
                      "masterWidth": 1920,
                      "masterHeight": 1080,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/56A9C8DA09747B319C6C419244665A8828C3F59B3469DD98261F9079B8D90360"
                    }
                  }
                }
              },
              "background_details": {
                "1.33": {
                  "series": {
                    "default": {
                      "masterId": "687D2F30F2DE4D3A55889109547F0A6CA82BA371B6FB3F4D3641F2F67D2739A4",
                      "masterWidth": 2880,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/687D2F30F2DE4D3A55889109547F0A6CA82BA371B6FB3F4D3641F2F67D2739A4"
                    }
                  }
                },
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1"
                    }
                  }
                }
              }
            },
            "labels": [
              {
                "region": "JP",
                "value": "smoking_disclaimer"
              },
              {
                "region": "JP",
                "value": "pse_disclaimer"
              }
            ],
            "league": null,
            "mediaMetadata": {
              "activeAspectRatio": 1.78,
              "audioTracks": [
                {
                  "features": [
                    "dolby_20"
                  ],
                  "language": "ja",
                  "name": null,
                  "renditionName": "Japanese",
                  "trackType": "PRIMARY"
                }
              ],
              "captions": [
                {
                  "language": "zh-Hant",
                  "name": null,
                  "renditionName": "Chinese (Traditional)",
                  "trackType": "NORMAL"
                },
                {
                  "language": "ja",
                  "name": null,
                  "renditionName": "Japanese [CC]",
                  "trackType": "SDH"
                },
                {
                  "language": "en",
                  "name": null,
                  "renditionName": "English",
                  "trackType": "NORMAL"
                }
              ],
              "facets": [
                {
                  "activeAspectRatio": 1.78,
                  "label": "default"
                }
              ],
              "features": [
                "sdr",
                "hdr"
              ],
              "format": "HD",
              "mediaId": "b1144226-44ac-423a-9efb-dde59c281e53",
              "phase": "active",
              "playbackUrls": [
                {
                  "rel": "video",
                  "href": "https://disney.playback.edge.bamgrid.com/media/b1144226-44ac-423a-9efb-dde59c281e53/scenarios/{scenario}",
                  "templated": true,
                  "params": [
                    {
                      "name": "scenario",
                      "description": "Playback scenario"
                    }
                  ]
                }
              ],
              "productType": "VOD",
              "runtimeMillis": 1472000,
              "state": "ON",
              "type": "VIDEO"
            },
            "meta": null,
            "mediaRights": {
              "violations": [],
              "downloadBlocked": false,
              "pconBlocked": false,
              "rewind": true
            },
            "milestone": {
              "FFOC": [
                {
                  "id": "36d6ec2b-0d9d-47df-9ace-43f8c1f9d272",
                  "milestoneTime": [
                    {
                      "startMillis": 1001,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "FFEI": [
                {
                  "id": "e5bd25ff-b736-4062-a99b-93a7d5d04527",
                  "milestoneTime": [
                    {
                      "startMillis": 67985,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "intro_start": [
                {
                  "id": "866a271b-e62a-4693-a1c0-d1f732f4e38e",
                  "milestoneTime": [
                    {
                      "startMillis": 67985,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "intro_end": [
                {
                  "id": "628fe4f5-f3a6-4df3-96bb-32b431a7ed86",
                  "milestoneTime": [
                    {
                      "startMillis": 158033,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "FFEC": [
                {
                  "id": "b4ede8b5-0dda-40db-81df-cf88c915f7db",
                  "milestoneTime": [
                    {
                      "startMillis": 1371079,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "up_next": [
                {
                  "id": "2e0d434a-06bc-40ac-966e-fca7b3c90d3e",
                  "milestoneTime": [
                    {
                      "startMillis": 1376084,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "LFEC": [
                {
                  "id": "c8401239-33f1-48b7-b243-dd261a88dadf",
                  "milestoneTime": [
                    {
                      "startMillis": 1461044,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "LFOC": [
                {
                  "id": "ec4e89d1-8a6a-4127-a2f3-049ace34e54c",
                  "milestoneTime": [
                    {
                      "startMillis": 1471054,
                      "type": "offset"
                    }
                  ]
                }
              ]
            },
            "originalLanguage": "ja",
            "participant": {
              "Actor": [
                {
                  "characterDetails": {
                    "character": "フリーレン",
                    "characterId": "322795247"
                  },
                  "displayName": "Atsumi Tanezaki",
                  "order": 1,
                  "participantId": "86906036",
                  "sortName": "敦美, 種﨑"
                },
                {
                  "characterDetails": {
                    "character": "フェルン",
                    "characterId": "322795246"
                  },
                  "displayName": "Kana Ichinose",
                  "order": 2,
                  "participantId": "190908111",
                  "sortName": "加那, 市ノ瀬"
                },
                {
                  "characterDetails": {
                    "character": "シュタルク",
                    "characterId": "322795346"
                  },
                  "displayName": "Chiaki Kobayashi",
                  "order": 3,
                  "participantId": "193439222",
                  "sortName": "千晃, 小林"
                },
                {
                  "characterDetails": {
                    "character": "ヒンメル",
                    "characterId": "322818264"
                  },
                  "displayName": "Nobuhiko Okamoto",
                  "order": 4,
                  "participantId": "189507914",
                  "sortName": "信彦, 岡本"
                },
                {
                  "characterDetails": {
                    "character": "ハイター",
                    "characterId": "322818265"
                  },
                  "displayName": "Hiroki Tochi",
                  "order": 5,
                  "participantId": "23219",
                  "sortName": "宏樹, 東地"
                },
                {
                  "characterDetails": {
                    "character": "アイゼン",
                    "characterId": "322823042"
                  },
                  "displayName": "Youji Ueda",
                  "order": 6,
                  "participantId": "42663081",
                  "sortName": "燿司, 上田"
                }
              ]
            },
            "programId": "84fa0469-e4de-4aac-813a-7bd824b66784",
            "programType": "episode",
            "ratings": [
              {
                "advisories": [
                  "Violence-Some"
                ],
                "description": null,
                "filingNumber": null,
                "system": "Custom:DisneyPlus:APAC",
                "value": "12+"
              }
            ],
            "releases": [
              {
                "releaseDate": "2023-11-03",
                "releaseOrg": null,
                "releaseType": "original",
                "releaseYear": 2023,
                "territory": null
              }
            ],
            "seasonId": "1eed1274-c21f-43b4-8c1d-fdb0249e74af",
            "seasonSequenceNumber": 1,
            "seriesId": "985af96c-1678-4907-92ca-84880f812456",
            "seriesType": "standard",
            "sport": null,
            "tags": [
              {
                "displayName": null,
                "type": "disneyPlusOriginal",
                "value": "false"
              },
              {
                "displayName": null,
                "type": "titleEidr",
                "value": "9EB8-797D-BBB2-0BC4-3190-8"
              }
            ],
            "targetLanguage": "ja",
            "text": {
              "title": {
                "full": {
                  "series": {
                    "default": {
                      "content": "Frieren: Beyond Journey's End",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "A Powerful Mage",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                },
                "slug": {
                  "series": {
                    "default": {
                      "content": "frieren-beyond-journeys-end",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "a-powerful-mage",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                }
              },
              "description": {
                "medium": {
                  "series": {
                    "default": {
                      "content": "Elven mage Frieren defeats Demon Lord with hero Himmel's party. 50 years later, she returns to find Himmel aged and dying. Realizing her detachment from humanity, Frieren embarks on a journey to understand mortal life, meeting diverse people and facing various challenges along the way.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "The great mage Flamme lived over a thousand years ago, and is historically considered a hero despite being only human. One day she met Frieren, a lone survivor of an elven village that was destroyed by the Demon King's army. Meanwhile, the battle between Frieren and Aura reaches its climax.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                },
                "full": {
                  "program": {
                    "default": {
                      "content": "The great mage Flamme lived over a thousand years ago, and is historically considered a hero despite being only human. One day she met Frieren, a lone survivor of an elven village that was destroyed by the Demon King's army. Meanwhile, the battle between Frieren and Aura reaches its climax.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  },
                  "series": {
                    "default": {
                      "content": "Watch the new episode now.\n\nSome flashing lights sequences or patterns may affect photosensitive viewers.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  }
                },
                "brief": {
                  "series": {
                    "default": {
                      "content": "Elven mage Frieren embarks on a journey to understand humanity's mortality in an era of peace.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "Frieren and Aura's battle reaches climax while Frieren recalls when she met the great mage Flamme.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                }
              }
            },
            "type": "DmcVideo",
            "typedGenres": [],
            "videoArt": [],
            "videoId": "5adc86a0-50e4-4ed2-a595-d7d56f497ed7"
          },
          {
            "badging": null,
            "callToAction": null,
            "channel": null,
            "contentId": "520f4ce5-9477-4ce4-bffd-8fb186cefcba",
            "contentType": "full",
            "currentAvailability": {
              "region": "JP",
              "kidsMode": false
            },
            "event": null,
            "encodedSeriesId": "1rlaH8IM0pkQ",
            "episodeNumber": null,
            "episodeSequenceNumber": 11,
            "episodeSeriesSequenceNumber": 11,
            "family": {
              "encodedFamilyId": "6UQd8W3WM6BQ",
              "familyId": "ZGlzbmV5b3JnOmRpc25leS5jb206cmFkYXI6NTIwODEw",
              "parent": true,
              "parentRef": {
                "encodedSeriesId": "1rlaH8IM0pkQ",
                "programId": "4908cdc4-05f7-4628-bd72-1ebd7089210e",
                "seasonId": "1eed1274-c21f-43b4-8c1d-fdb0249e74af",
                "seriesId": "985af96c-1678-4907-92ca-84880f812456"
              },
              "sequenceNumber": null
            },
            "groups": [
              {
                "name": "Non-TWDC",
                "partnerGroupId": "401208",
                "type": "disneyPlusStorefrontSubBrand"
              },
              {
                "name": "Star",
                "partnerGroupId": "377148",
                "type": "disneyPlusStorefrontBrand"
              }
            ],
            "internalTitle": "Frieren: Beyond Journey's End - s1e11 - 520f4ce5-9477-4ce4-bffd-8fb186cefcba",
            "image": {
              "title_treatment": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "BD389E7A5EF75EB8CFDAB05C134C97232D6F8C097D0C91C3518096BB56463910",
                      "masterWidth": 1920,
                      "masterHeight": 1080,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/BD389E7A5EF75EB8CFDAB05C134C97232D6F8C097D0C91C3518096BB56463910"
                    }
                  }
                }
              },
              "tile": {
                "0.71": {
                  "series": {
                    "default": {
                      "masterId": "77CC1FC69866834FEE4B724A07A163CA65825CB75736BD3589AF6FDA2B6A74EA",
                      "masterWidth": 2000,
                      "masterHeight": 2818,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/77CC1FC69866834FEE4B724A07A163CA65825CB75736BD3589AF6FDA2B6A74EA"
                    }
                  }
                },
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "1129698D299F194FED20FEDC826413E9F0FA5281613BC57E7E645B359B3D56C7",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/1129698D299F194FED20FEDC826413E9F0FA5281613BC57E7E645B359B3D56C7"
                    }
                  }
                },
                "1.33": {
                  "series": {
                    "default": {
                      "masterId": "9F23483E3484C1BF8A4641819F2B18A657747B64A2B4BD7414287B11D0386B99",
                      "masterWidth": 2880,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/9F23483E3484C1BF8A4641819F2B18A657747B64A2B4BD7414287B11D0386B99"
                    }
                  }
                }
              },
              "background_up_next": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "0A0DA7884203201B1A13F29F8A52CCF4059F5E1377A10A0DF79951A3BF5F6B2C",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/0A0DA7884203201B1A13F29F8A52CCF4059F5E1377A10A0DF79951A3BF5F6B2C"
                    }
                  }
                }
              },
              "title_treatment_centered": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "56A9C8DA09747B319C6C419244665A8828C3F59B3469DD98261F9079B8D90360",
                      "masterWidth": 1920,
                      "masterHeight": 1080,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/56A9C8DA09747B319C6C419244665A8828C3F59B3469DD98261F9079B8D90360"
                    }
                  }
                }
              },
              "thumbnail": {
                "1.78": {
                  "program": {
                    "default": {
                      "masterId": "6F02A77B71D0E49E3E62A99C8E5F21D684CB5B9E5E3DECBD34F1313AFC19D8AA",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/6F02A77B71D0E49E3E62A99C8E5F21D684CB5B9E5E3DECBD34F1313AFC19D8AA"
                    }
                  }
                }
              },
              "background_details": {
                "1.33": {
                  "series": {
                    "default": {
                      "masterId": "687D2F30F2DE4D3A55889109547F0A6CA82BA371B6FB3F4D3641F2F67D2739A4",
                      "masterWidth": 2880,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/687D2F30F2DE4D3A55889109547F0A6CA82BA371B6FB3F4D3641F2F67D2739A4"
                    }
                  }
                },
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1"
                    }
                  }
                }
              }
            },
            "labels": [
              {
                "region": "JP",
                "value": "smoking_disclaimer"
              },
              {
                "region": "JP",
                "value": "pse_disclaimer"
              }
            ],
            "league": null,
            "mediaMetadata": {
              "activeAspectRatio": 1.78,
              "audioTracks": [
                {
                  "features": [
                    "dolby_20"
                  ],
                  "language": "ja",
                  "name": null,
                  "renditionName": "Japanese",
                  "trackType": "PRIMARY"
                }
              ],
              "captions": [
                {
                  "language": "zh-Hant",
                  "name": null,
                  "renditionName": "Chinese (Traditional)",
                  "trackType": "NORMAL"
                },
                {
                  "language": "ja",
                  "name": null,
                  "renditionName": "Japanese [CC]",
                  "trackType": "SDH"
                },
                {
                  "language": "en",
                  "name": null,
                  "renditionName": "English",
                  "trackType": "NORMAL"
                }
              ],
              "facets": [
                {
                  "activeAspectRatio": 1.78,
                  "label": "default"
                }
              ],
              "features": [
                "sdr",
                "hdr"
              ],
              "format": "HD",
              "mediaId": "c79a0e8d-3f32-466d-8c8f-f5733d4880b3",
              "phase": "active",
              "playbackUrls": [
                {
                  "rel": "video",
                  "href": "https://disney.playback.edge.bamgrid.com/media/c79a0e8d-3f32-466d-8c8f-f5733d4880b3/scenarios/{scenario}",
                  "templated": true,
                  "params": [
                    {
                      "name": "scenario",
                      "description": "Playback scenario"
                    }
                  ]
                }
              ],
              "productType": "VOD",
              "runtimeMillis": 1471000,
              "state": "ON",
              "type": "VIDEO"
            },
            "meta": null,
            "mediaRights": {
              "violations": [],
              "downloadBlocked": false,
              "pconBlocked": false,
              "rewind": true
            },
            "milestone": {
              "FFOC": [
                {
                  "id": "277527ab-33f2-414e-b741-90a21e60c0f6",
                  "milestoneTime": [
                    {
                      "startMillis": 1001,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "FFEI": [
                {
                  "id": "42b8540e-7dd1-4d8f-89ba-cc75c59e84d1",
                  "milestoneTime": [
                    {
                      "startMillis": 48048,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "intro_start": [
                {
                  "id": "795ab831-3054-466a-80ab-c5970eba5da4",
                  "milestoneTime": [
                    {
                      "startMillis": 48048,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "intro_end": [
                {
                  "id": "fa894813-b03a-4f35-95e5-9f0930125b11",
                  "milestoneTime": [
                    {
                      "startMillis": 138013,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "FFEC": [
                {
                  "id": "3b33ac7c-ec84-4b6a-adc8-fa82cd6f0994",
                  "milestoneTime": [
                    {
                      "startMillis": 1370996,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "up_next": [
                {
                  "id": "81a801e8-65a8-42dc-9aa0-176bb22d7cde",
                  "milestoneTime": [
                    {
                      "startMillis": 1376001,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "LFEC": [
                {
                  "id": "ed994ac5-651c-4b93-ab3d-e716e6b47e06",
                  "milestoneTime": [
                    {
                      "startMillis": 1461044,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "LFOC": [
                {
                  "id": "bce6e0aa-401b-4cf8-997e-3289a30e5133",
                  "milestoneTime": [
                    {
                      "startMillis": 1470971,
                      "type": "offset"
                    }
                  ]
                }
              ]
            },
            "originalLanguage": "ja",
            "participant": {
              "Actor": [
                {
                  "characterDetails": {
                    "character": "フリーレン",
                    "characterId": "322795247"
                  },
                  "displayName": "Atsumi Tanezaki",
                  "order": 1,
                  "participantId": "86906036",
                  "sortName": "敦美, 種﨑"
                },
                {
                  "characterDetails": {
                    "character": "フェルン",
                    "characterId": "322795246"
                  },
                  "displayName": "Kana Ichinose",
                  "order": 2,
                  "participantId": "190908111",
                  "sortName": "加那, 市ノ瀬"
                },
                {
                  "characterDetails": {
                    "character": "シュタルク",
                    "characterId": "322795346"
                  },
                  "displayName": "Chiaki Kobayashi",
                  "order": 3,
                  "participantId": "193439222",
                  "sortName": "千晃, 小林"
                },
                {
                  "characterDetails": {
                    "character": "ヒンメル",
                    "characterId": "322818264"
                  },
                  "displayName": "Nobuhiko Okamoto",
                  "order": 4,
                  "participantId": "189507914",
                  "sortName": "信彦, 岡本"
                },
                {
                  "characterDetails": {
                    "character": "ハイター",
                    "characterId": "322818265"
                  },
                  "displayName": "Hiroki Tochi",
                  "order": 5,
                  "participantId": "23219",
                  "sortName": "宏樹, 東地"
                },
                {
                  "characterDetails": {
                    "character": "アイゼン",
                    "characterId": "322823042"
                  },
                  "displayName": "Youji Ueda",
                  "order": 6,
                  "participantId": "42663081",
                  "sortName": "燿司, 上田"
                }
              ]
            },
            "programId": "4908cdc4-05f7-4628-bd72-1ebd7089210e",
            "programType": "episode",
            "ratings": [
              {
                "advisories": [
                  "Violence-Some"
                ],
                "description": null,
                "filingNumber": null,
                "system": "Custom:DisneyPlus:APAC",
                "value": "12+"
              }
            ],
            "releases": [
              {
                "releaseDate": "2023-11-10",
                "releaseOrg": null,
                "releaseType": "original",
                "releaseYear": 2023,
                "territory": null
              }
            ],
            "seasonId": "1eed1274-c21f-43b4-8c1d-fdb0249e74af",
            "seasonSequenceNumber": 1,
            "seriesId": "985af96c-1678-4907-92ca-84880f812456",
            "seriesType": "standard",
            "sport": null,
            "tags": [
              {
                "displayName": null,
                "type": "titleEidr",
                "value": "B9A3-DA57-BF45-701F-7DB3-D"
              },
              {
                "displayName": null,
                "type": "disneyPlusOriginal",
                "value": "false"
              }
            ],
            "targetLanguage": "ja",
            "text": {
              "description": {
                "medium": {
                  "program": {
                    "default": {
                      "content": "Frieren, Fern, and Stark defeated Aura and her army. Graf Granat gave the highest gratitude to Frieren for bringing peace and holding a funeral for the men who were once under Aura's control. They continued on their journey, but the winter on the road to the Northern Lands was harsher than expected.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  },
                  "series": {
                    "default": {
                      "content": "Elven mage Frieren defeats Demon Lord with hero Himmel's party. 50 years later, she returns to find Himmel aged and dying. Realizing her detachment from humanity, Frieren embarks on a journey to understand mortal life, meeting diverse people and facing various challenges along the way.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  }
                },
                "full": {
                  "program": {
                    "default": {
                      "content": "Frieren, Fern, and Stark defeated Aura and her army. Graf Granat gave the highest gratitude to Frieren for bringing peace and holding a funeral for the men who were once under Aura's control. They continued on their journey, but the winter on the road to the Northern Lands was harsher than expected.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  },
                  "series": {
                    "default": {
                      "content": "Watch the new episode now.\n\nSome flashing lights sequences or patterns may affect photosensitive viewers.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  }
                },
                "brief": {
                  "series": {
                    "default": {
                      "content": "Elven mage Frieren embarks on a journey to understand humanity's mortality in an era of peace.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "Frieren, Fern, and Stark struggle on the road to the Northern Lands in a harsh winter.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                }
              },
              "title": {
                "full": {
                  "series": {
                    "default": {
                      "content": "Frieren: Beyond Journey's End",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "Winter in the Northern Lands",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                },
                "slug": {
                  "series": {
                    "default": {
                      "content": "frieren-beyond-journeys-end",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "winter-in-the-northern-lands",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                }
              }
            },
            "type": "DmcVideo",
            "typedGenres": [],
            "videoArt": [],
            "videoId": "1c444c99-b138-4726-aed0-191c095fc5ac"
          },
          {
            "badging": null,
            "callToAction": null,
            "channel": null,
            "contentId": "37847218-aec9-47b8-8fa9-1e2f795ef448",
            "contentType": "full",
            "currentAvailability": {
              "region": "JP",
              "kidsMode": false
            },
            "event": null,
            "encodedSeriesId": "1rlaH8IM0pkQ",
            "episodeNumber": null,
            "episodeSequenceNumber": 12,
            "episodeSeriesSequenceNumber": 12,
            "family": {
              "encodedFamilyId": "3hcbQN03yNKX",
              "familyId": "ZGlzbmV5b3JnOmRpc25leS5jb206cmFkYXI6NTIwODEx",
              "parent": true,
              "parentRef": {
                "encodedSeriesId": "1rlaH8IM0pkQ",
                "programId": "2f2bc3a2-4376-4918-98d4-138fe49dca5a",
                "seasonId": "1eed1274-c21f-43b4-8c1d-fdb0249e74af",
                "seriesId": "985af96c-1678-4907-92ca-84880f812456"
              },
              "sequenceNumber": null
            },
            "groups": [
              {
                "name": "Non-TWDC",
                "partnerGroupId": "401208",
                "type": "disneyPlusStorefrontSubBrand"
              },
              {
                "name": "Star",
                "partnerGroupId": "377148",
                "type": "disneyPlusStorefrontBrand"
              }
            ],
            "internalTitle": "Frieren: Beyond Journey's End - s1e12 - 37847218-aec9-47b8-8fa9-1e2f795ef448",
            "image": {
              "title_treatment": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "BD389E7A5EF75EB8CFDAB05C134C97232D6F8C097D0C91C3518096BB56463910",
                      "masterWidth": 1920,
                      "masterHeight": 1080,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/BD389E7A5EF75EB8CFDAB05C134C97232D6F8C097D0C91C3518096BB56463910"
                    }
                  }
                }
              },
              "tile": {
                "0.71": {
                  "series": {
                    "default": {
                      "masterId": "77CC1FC69866834FEE4B724A07A163CA65825CB75736BD3589AF6FDA2B6A74EA",
                      "masterWidth": 2000,
                      "masterHeight": 2818,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/77CC1FC69866834FEE4B724A07A163CA65825CB75736BD3589AF6FDA2B6A74EA"
                    }
                  }
                },
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "1129698D299F194FED20FEDC826413E9F0FA5281613BC57E7E645B359B3D56C7",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/1129698D299F194FED20FEDC826413E9F0FA5281613BC57E7E645B359B3D56C7"
                    }
                  }
                },
                "1.33": {
                  "series": {
                    "default": {
                      "masterId": "9F23483E3484C1BF8A4641819F2B18A657747B64A2B4BD7414287B11D0386B99",
                      "masterWidth": 2880,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/9F23483E3484C1BF8A4641819F2B18A657747B64A2B4BD7414287B11D0386B99"
                    }
                  }
                }
              },
              "background_up_next": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "0A0DA7884203201B1A13F29F8A52CCF4059F5E1377A10A0DF79951A3BF5F6B2C",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/0A0DA7884203201B1A13F29F8A52CCF4059F5E1377A10A0DF79951A3BF5F6B2C"
                    }
                  }
                }
              },
              "title_treatment_centered": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "56A9C8DA09747B319C6C419244665A8828C3F59B3469DD98261F9079B8D90360",
                      "masterWidth": 1920,
                      "masterHeight": 1080,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/56A9C8DA09747B319C6C419244665A8828C3F59B3469DD98261F9079B8D90360"
                    }
                  }
                }
              },
              "background_details": {
                "1.33": {
                  "series": {
                    "default": {
                      "masterId": "687D2F30F2DE4D3A55889109547F0A6CA82BA371B6FB3F4D3641F2F67D2739A4",
                      "masterWidth": 2880,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/687D2F30F2DE4D3A55889109547F0A6CA82BA371B6FB3F4D3641F2F67D2739A4"
                    }
                  }
                },
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1"
                    }
                  }
                }
              },
              "thumbnail": {
                "1.78": {
                  "program": {
                    "default": {
                      "masterId": "DDAEA213CB749D97EB73F2358DF0DB260E23A5BB2BDA0B0868E68224051A22FB",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/DDAEA213CB749D97EB73F2358DF0DB260E23A5BB2BDA0B0868E68224051A22FB"
                    }
                  }
                }
              }
            },
            "labels": [
              {
                "region": "JP",
                "value": "smoking_disclaimer"
              },
              {
                "region": "JP",
                "value": "pse_disclaimer"
              }
            ],
            "league": null,
            "mediaMetadata": {
              "activeAspectRatio": 1.78,
              "audioTracks": [
                {
                  "features": [
                    "dolby_20"
                  ],
                  "language": "ja",
                  "name": null,
                  "renditionName": "Japanese",
                  "trackType": "PRIMARY"
                }
              ],
              "captions": [
                {
                  "language": "zh-Hant",
                  "name": null,
                  "renditionName": "Chinese (Traditional)",
                  "trackType": "NORMAL"
                },
                {
                  "language": "ja",
                  "name": null,
                  "renditionName": "Japanese [CC]",
                  "trackType": "SDH"
                },
                {
                  "language": "en",
                  "name": null,
                  "renditionName": "English",
                  "trackType": "NORMAL"
                }
              ],
              "facets": [
                {
                  "activeAspectRatio": 1.78,
                  "label": "default"
                }
              ],
              "features": [
                "sdr",
                "hdr"
              ],
              "format": "HD",
              "mediaId": "a8c77efb-0797-4a61-8cd2-9e4f4566e323",
              "phase": "active",
              "playbackUrls": [
                {
                  "rel": "video",
                  "href": "https://disney.playback.edge.bamgrid.com/media/a8c77efb-0797-4a61-8cd2-9e4f4566e323/scenarios/{scenario}",
                  "templated": true,
                  "params": [
                    {
                      "name": "scenario",
                      "description": "Playback scenario"
                    }
                  ]
                }
              ],
              "productType": "VOD",
              "runtimeMillis": 1472000,
              "state": "ON",
              "type": "VIDEO"
            },
            "meta": null,
            "mediaRights": {
              "violations": [],
              "downloadBlocked": false,
              "pconBlocked": false,
              "rewind": true
            },
            "milestone": {
              "FFEI": [
                {
                  "id": "85334e7d-8af6-4bd0-ab4c-666828f54950",
                  "milestoneTime": [
                    {
                      "startMillis": 1043,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "FFOC": [
                {
                  "id": "1b6f2f23-b468-4e98-a41f-3ab22ab74599",
                  "milestoneTime": [
                    {
                      "startMillis": 1001,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "intro_start": [
                {
                  "id": "39c7822c-76f7-4a2a-8921-99ec702c56d5",
                  "milestoneTime": [
                    {
                      "startMillis": 1043,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "intro_end": [
                {
                  "id": "5345e206-cb7f-4a2a-bd79-f4ab8424db9d",
                  "milestoneTime": [
                    {
                      "startMillis": 91008,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "FFEC": [
                {
                  "id": "346d6015-ada2-4bdb-a4c6-9cd2e12948ed",
                  "milestoneTime": [
                    {
                      "startMillis": 1371079,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "up_next": [
                {
                  "id": "78107b71-3b00-40fb-8eaa-269134e4d17e",
                  "milestoneTime": [
                    {
                      "startMillis": 1376084,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "LFEC": [
                {
                  "id": "0d0a65c8-6c84-495b-b65c-f53acfbbbf8e",
                  "milestoneTime": [
                    {
                      "startMillis": 1461044,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "LFOC": [
                {
                  "id": "6ba3eaf4-b6b8-44c3-8419-a38ae50e7584",
                  "milestoneTime": [
                    {
                      "startMillis": 1471054,
                      "type": "offset"
                    }
                  ]
                }
              ]
            },
            "originalLanguage": "ja",
            "participant": {
              "Actor": [
                {
                  "characterDetails": {
                    "character": "フリーレン",
                    "characterId": "322795247"
                  },
                  "displayName": "Atsumi Tanezaki",
                  "order": 1,
                  "participantId": "86906036",
                  "sortName": "敦美, 種﨑"
                },
                {
                  "characterDetails": {
                    "character": "フェルン",
                    "characterId": "322795246"
                  },
                  "displayName": "Kana Ichinose",
                  "order": 2,
                  "participantId": "190908111",
                  "sortName": "加那, 市ノ瀬"
                },
                {
                  "characterDetails": {
                    "character": "シュタルク",
                    "characterId": "322795346"
                  },
                  "displayName": "Chiaki Kobayashi",
                  "order": 3,
                  "participantId": "193439222",
                  "sortName": "千晃, 小林"
                },
                {
                  "characterDetails": {
                    "character": "ヒンメル",
                    "characterId": "322818264"
                  },
                  "displayName": "Nobuhiko Okamoto",
                  "order": 4,
                  "participantId": "189507914",
                  "sortName": "信彦, 岡本"
                },
                {
                  "characterDetails": {
                    "character": "ハイター",
                    "characterId": "322818265"
                  },
                  "displayName": "Hiroki Tochi",
                  "order": 5,
                  "participantId": "23219",
                  "sortName": "宏樹, 東地"
                },
                {
                  "characterDetails": {
                    "character": "アイゼン",
                    "characterId": "322823042"
                  },
                  "displayName": "Youji Ueda",
                  "order": 6,
                  "participantId": "42663081",
                  "sortName": "燿司, 上田"
                }
              ]
            },
            "programId": "2f2bc3a2-4376-4918-98d4-138fe49dca5a",
            "programType": "episode",
            "ratings": [
              {
                "advisories": [
                  "Violence-Some"
                ],
                "description": null,
                "filingNumber": null,
                "system": "Custom:DisneyPlus:APAC",
                "value": "12+"
              }
            ],
            "releases": [
              {
                "releaseDate": "2023-11-17",
                "releaseOrg": null,
                "releaseType": "original",
                "releaseYear": 2023,
                "territory": null
              }
            ],
            "seasonId": "1eed1274-c21f-43b4-8c1d-fdb0249e74af",
            "seasonSequenceNumber": 1,
            "seriesId": "985af96c-1678-4907-92ca-84880f812456",
            "seriesType": "standard",
            "sport": null,
            "tags": [
              {
                "displayName": null,
                "type": "disneyPlusOriginal",
                "value": "false"
              },
              {
                "displayName": null,
                "type": "titleEidr",
                "value": "C1F2-EDBD-99EC-575C-AA0B-E"
              }
            ],
            "targetLanguage": "ja",
            "text": {
              "title": {
                "full": {
                  "series": {
                    "default": {
                      "content": "Frieren: Beyond Journey's End",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "A Real Hero",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                },
                "slug": {
                  "program": {
                    "default": {
                      "content": "a-real-hero",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  },
                  "series": {
                    "default": {
                      "content": "frieren-beyond-journeys-end",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  }
                }
              },
              "description": {
                "medium": {
                  "program": {
                    "default": {
                      "content": "Frieren and the others arrived at the Village of the Sword. It was a place where 80 years ago Himmel pulled the \"Sword of the Hero\" that can only be pulled by the hero that would drive away the calamity that will destroy the world. Memories from 80 years ago start coming back to Frieren's mind.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  },
                  "series": {
                    "default": {
                      "content": "Elven mage Frieren defeats Demon Lord with hero Himmel's party. 50 years later, she returns to find Himmel aged and dying. Realizing her detachment from humanity, Frieren embarks on a journey to understand mortal life, meeting diverse people and facing various challenges along the way.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  }
                },
                "full": {
                  "program": {
                    "default": {
                      "content": "Frieren and the others arrived at the Village of the Sword. It was a place where 80 years ago Himmel pulled the \"Sword of the Hero\" that can only be pulled by the hero that would drive away the calamity that will destroy the world. Memories from 80 years ago start coming back to Frieren's mind.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  },
                  "series": {
                    "default": {
                      "content": "Watch the new episode now.\n\nSome flashing lights sequences or patterns may affect photosensitive viewers.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  }
                },
                "brief": {
                  "series": {
                    "default": {
                      "content": "Elven mage Frieren embarks on a journey to understand humanity's mortality in an era of peace.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "Frieren and the others arrive at a village where Himmel once pulled the sword of the hero.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                }
              }
            },
            "type": "DmcVideo",
            "typedGenres": [],
            "videoArt": [],
            "videoId": "09e6af65-be05-4ea9-8473-4ea28ff2829a"
          },
          {
            "badging": null,
            "callToAction": null,
            "channel": null,
            "contentId": "552f4da6-a74a-47af-8d8e-d1ce5a8986e3",
            "contentType": "full",
            "currentAvailability": {
              "region": "JP",
              "kidsMode": false
            },
            "event": null,
            "encodedSeriesId": "1rlaH8IM0pkQ",
            "episodeNumber": null,
            "episodeSequenceNumber": 13,
            "episodeSeriesSequenceNumber": 13,
            "family": {
              "encodedFamilyId": "1Ugh9APBRgOv",
              "familyId": "ZGlzbmV5b3JnOmRpc25leS5jb206cmFkYXI6NTIwODEy",
              "parent": true,
              "parentRef": {
                "encodedSeriesId": "1rlaH8IM0pkQ",
                "programId": "40086ca7-4bca-46c6-924d-77469d82c6c6",
                "seasonId": "1eed1274-c21f-43b4-8c1d-fdb0249e74af",
                "seriesId": "985af96c-1678-4907-92ca-84880f812456"
              },
              "sequenceNumber": null
            },
            "groups": [
              {
                "name": "Non-TWDC",
                "partnerGroupId": "401208",
                "type": "disneyPlusStorefrontSubBrand"
              },
              {
                "name": "Star",
                "partnerGroupId": "377148",
                "type": "disneyPlusStorefrontBrand"
              }
            ],
            "internalTitle": "Frieren: Beyond Journey's End - s1e13 - 552f4da6-a74a-47af-8d8e-d1ce5a8986e3",
            "image": {
              "title_treatment": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "BD389E7A5EF75EB8CFDAB05C134C97232D6F8C097D0C91C3518096BB56463910",
                      "masterWidth": 1920,
                      "masterHeight": 1080,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/BD389E7A5EF75EB8CFDAB05C134C97232D6F8C097D0C91C3518096BB56463910"
                    }
                  }
                }
              },
              "tile": {
                "0.71": {
                  "series": {
                    "default": {
                      "masterId": "77CC1FC69866834FEE4B724A07A163CA65825CB75736BD3589AF6FDA2B6A74EA",
                      "masterWidth": 2000,
                      "masterHeight": 2818,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/77CC1FC69866834FEE4B724A07A163CA65825CB75736BD3589AF6FDA2B6A74EA"
                    }
                  }
                },
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "1129698D299F194FED20FEDC826413E9F0FA5281613BC57E7E645B359B3D56C7",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/1129698D299F194FED20FEDC826413E9F0FA5281613BC57E7E645B359B3D56C7"
                    }
                  }
                },
                "1.33": {
                  "series": {
                    "default": {
                      "masterId": "9F23483E3484C1BF8A4641819F2B18A657747B64A2B4BD7414287B11D0386B99",
                      "masterWidth": 2880,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/9F23483E3484C1BF8A4641819F2B18A657747B64A2B4BD7414287B11D0386B99"
                    }
                  }
                }
              },
              "background_up_next": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "0A0DA7884203201B1A13F29F8A52CCF4059F5E1377A10A0DF79951A3BF5F6B2C",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/0A0DA7884203201B1A13F29F8A52CCF4059F5E1377A10A0DF79951A3BF5F6B2C"
                    }
                  }
                }
              },
              "title_treatment_centered": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "56A9C8DA09747B319C6C419244665A8828C3F59B3469DD98261F9079B8D90360",
                      "masterWidth": 1920,
                      "masterHeight": 1080,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/56A9C8DA09747B319C6C419244665A8828C3F59B3469DD98261F9079B8D90360"
                    }
                  }
                }
              },
              "thumbnail": {
                "1.78": {
                  "program": {
                    "default": {
                      "masterId": "18D96B99F79522D655AC1250F6CB610FF5BB75DE58747C1FEE3D4543190D69DB",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/18D96B99F79522D655AC1250F6CB610FF5BB75DE58747C1FEE3D4543190D69DB"
                    }
                  }
                }
              },
              "background_details": {
                "1.33": {
                  "series": {
                    "default": {
                      "masterId": "687D2F30F2DE4D3A55889109547F0A6CA82BA371B6FB3F4D3641F2F67D2739A4",
                      "masterWidth": 2880,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/687D2F30F2DE4D3A55889109547F0A6CA82BA371B6FB3F4D3641F2F67D2739A4"
                    }
                  }
                },
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1"
                    }
                  }
                }
              }
            },
            "labels": [
              {
                "region": "JP",
                "value": "smoking_disclaimer"
              },
              {
                "region": "JP",
                "value": "pse_disclaimer"
              }
            ],
            "league": null,
            "mediaMetadata": {
              "activeAspectRatio": 1.78,
              "audioTracks": [
                {
                  "features": [
                    "dolby_20"
                  ],
                  "language": "ja",
                  "name": null,
                  "renditionName": "Japanese",
                  "trackType": "PRIMARY"
                }
              ],
              "captions": [
                {
                  "language": "zh-Hant",
                  "name": null,
                  "renditionName": "Chinese (Traditional)",
                  "trackType": "NORMAL"
                },
                {
                  "language": "ja",
                  "name": null,
                  "renditionName": "Japanese [CC]",
                  "trackType": "SDH"
                },
                {
                  "language": "en",
                  "name": null,
                  "renditionName": "English",
                  "trackType": "NORMAL"
                }
              ],
              "facets": [
                {
                  "activeAspectRatio": 1.78,
                  "label": "default"
                }
              ],
              "features": [
                "sdr",
                "hdr"
              ],
              "format": "HD",
              "mediaId": "6c49ecd1-3b0f-4894-9479-38e1b6d51095",
              "phase": "active",
              "playbackUrls": [
                {
                  "rel": "video",
                  "href": "https://disney.playback.edge.bamgrid.com/media/6c49ecd1-3b0f-4894-9479-38e1b6d51095/scenarios/{scenario}",
                  "templated": true,
                  "params": [
                    {
                      "name": "scenario",
                      "description": "Playback scenario"
                    }
                  ]
                }
              ],
              "productType": "VOD",
              "runtimeMillis": 1472000,
              "state": "ON",
              "type": "VIDEO"
            },
            "meta": null,
            "mediaRights": {
              "violations": [],
              "downloadBlocked": false,
              "pconBlocked": false,
              "rewind": true
            },
            "milestone": {
              "FFOC": [
                {
                  "id": "43027079-892e-4ad1-a423-672d3127e23d",
                  "milestoneTime": [
                    {
                      "startMillis": 1001,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "intro_start": [
                {
                  "id": "48af25d5-0d9b-4d32-821e-eed1a5b9baca",
                  "milestoneTime": [
                    {
                      "startMillis": 23023,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "FFEI": [
                {
                  "id": "2bf1d732-2d02-417b-9873-b935fbe4d899",
                  "milestoneTime": [
                    {
                      "startMillis": 23023,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "intro_end": [
                {
                  "id": "40b9d07d-4e16-400d-b151-8caf47f194ae",
                  "milestoneTime": [
                    {
                      "startMillis": 113030,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "FFEC": [
                {
                  "id": "dbc9e30e-dd64-4b82-bc18-992325c97eac",
                  "milestoneTime": [
                    {
                      "startMillis": 1371079,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "up_next": [
                {
                  "id": "060df0a7-6b55-4483-be75-61482d3cc4d4",
                  "milestoneTime": [
                    {
                      "startMillis": 1376084,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "LFEC": [
                {
                  "id": "05986ade-a889-4727-a2ac-15ca14af5f8a",
                  "milestoneTime": [
                    {
                      "startMillis": 1461044,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "LFOC": [
                {
                  "id": "805da7b8-8229-4408-b799-7a3c9656cbeb",
                  "milestoneTime": [
                    {
                      "startMillis": 1471054,
                      "type": "offset"
                    }
                  ]
                }
              ]
            },
            "originalLanguage": "ja",
            "participant": {
              "Actor": [
                {
                  "characterDetails": {
                    "character": "フリーレン",
                    "characterId": "322795247"
                  },
                  "displayName": "Atsumi Tanezaki",
                  "order": 1,
                  "participantId": "86906036",
                  "sortName": "敦美, 種﨑"
                },
                {
                  "characterDetails": {
                    "character": "フェルン",
                    "characterId": "322795246"
                  },
                  "displayName": "Kana Ichinose",
                  "order": 2,
                  "participantId": "190908111",
                  "sortName": "加那, 市ノ瀬"
                },
                {
                  "characterDetails": {
                    "character": "シュタルク",
                    "characterId": "322795346"
                  },
                  "displayName": "Chiaki Kobayashi",
                  "order": 3,
                  "participantId": "193439222",
                  "sortName": "千晃, 小林"
                },
                {
                  "characterDetails": {
                    "character": "ヒンメル",
                    "characterId": "322818264"
                  },
                  "displayName": "Nobuhiko Okamoto",
                  "order": 4,
                  "participantId": "189507914",
                  "sortName": "信彦, 岡本"
                },
                {
                  "characterDetails": {
                    "character": "ハイター",
                    "characterId": "322818265"
                  },
                  "displayName": "Hiroki Tochi",
                  "order": 5,
                  "participantId": "23219",
                  "sortName": "宏樹, 東地"
                },
                {
                  "characterDetails": {
                    "character": "アイゼン",
                    "characterId": "322823042"
                  },
                  "displayName": "Youji Ueda",
                  "order": 6,
                  "participantId": "42663081",
                  "sortName": "燿司, 上田"
                }
              ]
            },
            "programId": "40086ca7-4bca-46c6-924d-77469d82c6c6",
            "programType": "episode",
            "ratings": [
              {
                "advisories": [
                  "Violence-Some"
                ],
                "description": null,
                "filingNumber": null,
                "system": "Custom:DisneyPlus:APAC",
                "value": "12+"
              }
            ],
            "releases": [
              {
                "releaseDate": "2023-11-24",
                "releaseOrg": null,
                "releaseType": "original",
                "releaseYear": 2023,
                "territory": null
              }
            ],
            "seasonId": "1eed1274-c21f-43b4-8c1d-fdb0249e74af",
            "seasonSequenceNumber": 1,
            "seriesId": "985af96c-1678-4907-92ca-84880f812456",
            "seriesType": "standard",
            "sport": null,
            "tags": [
              {
                "displayName": null,
                "type": "disneyPlusOriginal",
                "value": "false"
              },
              {
                "displayName": null,
                "type": "titleEidr",
                "value": "384C-E590-1B8E-BBA0-47ED-K"
              }
            ],
            "targetLanguage": "ja",
            "text": {
              "title": {
                "full": {
                  "program": {
                    "default": {
                      "content": "Aversion to One's Own Kind",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  },
                  "series": {
                    "default": {
                      "content": "Frieren: Beyond Journey's End",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  }
                },
                "slug": {
                  "series": {
                    "default": {
                      "content": "frieren-beyond-journeys-end",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "aversion-to-ones-own-kind",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                }
              },
              "description": {
                "medium": {
                  "series": {
                    "default": {
                      "content": "Elven mage Frieren defeats Demon Lord with hero Himmel's party. 50 years later, she returns to find Himmel aged and dying. Realizing her detachment from humanity, Frieren embarks on a journey to understand mortal life, meeting diverse people and facing various challenges along the way.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "The group meets Sein, the younger brother of a priest of a church near the Alt Woods in the Northern Lands. Frieren is surprised to see how he can use advanced magic that can easily heal a hard-to-cure poison. They later heard that Sein once dreamed of becoming an adventurer.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                },
                "full": {
                  "program": {
                    "default": {
                      "content": "The group meets Sein, the younger brother of a priest of a church near the Alt Woods in the Northern Lands. Frieren is surprised to see how he can use advanced magic that can easily heal a hard-to-cure poison. They later heard that Sein once dreamed of becoming an adventurer.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  },
                  "series": {
                    "default": {
                      "content": "Watch the new episode now.\n\nSome flashing lights sequences or patterns may affect photosensitive viewers.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  }
                },
                "brief": {
                  "series": {
                    "default": {
                      "content": "Elven mage Frieren embarks on a journey to understand humanity's mortality in an era of peace.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "The group meets Sein, a talented priest who dreamed of being an adventurer but refuses to join them.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                }
              }
            },
            "type": "DmcVideo",
            "typedGenres": [],
            "videoArt": [],
            "videoId": "b9851b94-7a8d-4442-880e-70c516a873da"
          },
          {
            "badging": null,
            "callToAction": null,
            "channel": null,
            "contentId": "097260a2-e567-4198-b3e9-09a509ce04e9",
            "contentType": "full",
            "currentAvailability": {
              "region": "JP",
              "kidsMode": false
            },
            "event": null,
            "encodedSeriesId": "1rlaH8IM0pkQ",
            "episodeNumber": null,
            "episodeSequenceNumber": 14,
            "episodeSeriesSequenceNumber": 14,
            "family": {
              "encodedFamilyId": "2dLzUiMhtPc6",
              "familyId": "ZGlzbmV5b3JnOmRpc25leS5jb206cmFkYXI6NTIwODEz",
              "parent": true,
              "parentRef": {
                "encodedSeriesId": "1rlaH8IM0pkQ",
                "programId": "5f6ea159-96fc-4c4f-adda-55c7b111136a",
                "seasonId": "1eed1274-c21f-43b4-8c1d-fdb0249e74af",
                "seriesId": "985af96c-1678-4907-92ca-84880f812456"
              },
              "sequenceNumber": null
            },
            "groups": [
              {
                "name": "Non-TWDC",
                "partnerGroupId": "401208",
                "type": "disneyPlusStorefrontSubBrand"
              },
              {
                "name": "Star",
                "partnerGroupId": "377148",
                "type": "disneyPlusStorefrontBrand"
              }
            ],
            "internalTitle": "Frieren: Beyond Journey's End - s1e14 - 097260a2-e567-4198-b3e9-09a509ce04e9",
            "image": {
              "title_treatment": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "BD389E7A5EF75EB8CFDAB05C134C97232D6F8C097D0C91C3518096BB56463910",
                      "masterWidth": 1920,
                      "masterHeight": 1080,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/BD389E7A5EF75EB8CFDAB05C134C97232D6F8C097D0C91C3518096BB56463910"
                    }
                  }
                }
              },
              "tile": {
                "0.71": {
                  "series": {
                    "default": {
                      "masterId": "77CC1FC69866834FEE4B724A07A163CA65825CB75736BD3589AF6FDA2B6A74EA",
                      "masterWidth": 2000,
                      "masterHeight": 2818,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/77CC1FC69866834FEE4B724A07A163CA65825CB75736BD3589AF6FDA2B6A74EA"
                    }
                  }
                },
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "1129698D299F194FED20FEDC826413E9F0FA5281613BC57E7E645B359B3D56C7",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/1129698D299F194FED20FEDC826413E9F0FA5281613BC57E7E645B359B3D56C7"
                    }
                  }
                },
                "1.33": {
                  "series": {
                    "default": {
                      "masterId": "9F23483E3484C1BF8A4641819F2B18A657747B64A2B4BD7414287B11D0386B99",
                      "masterWidth": 2880,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/9F23483E3484C1BF8A4641819F2B18A657747B64A2B4BD7414287B11D0386B99"
                    }
                  }
                }
              },
              "thumbnail": {
                "1.78": {
                  "program": {
                    "default": {
                      "masterId": "145A4E2EF02069CD6248296DF3A6E671A934305E45120BB18E173337C17F1EC4",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/145A4E2EF02069CD6248296DF3A6E671A934305E45120BB18E173337C17F1EC4"
                    }
                  }
                }
              },
              "background_up_next": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "0A0DA7884203201B1A13F29F8A52CCF4059F5E1377A10A0DF79951A3BF5F6B2C",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/0A0DA7884203201B1A13F29F8A52CCF4059F5E1377A10A0DF79951A3BF5F6B2C"
                    }
                  }
                }
              },
              "title_treatment_centered": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "56A9C8DA09747B319C6C419244665A8828C3F59B3469DD98261F9079B8D90360",
                      "masterWidth": 1920,
                      "masterHeight": 1080,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/56A9C8DA09747B319C6C419244665A8828C3F59B3469DD98261F9079B8D90360"
                    }
                  }
                }
              },
              "background_details": {
                "1.33": {
                  "series": {
                    "default": {
                      "masterId": "687D2F30F2DE4D3A55889109547F0A6CA82BA371B6FB3F4D3641F2F67D2739A4",
                      "masterWidth": 2880,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/687D2F30F2DE4D3A55889109547F0A6CA82BA371B6FB3F4D3641F2F67D2739A4"
                    }
                  }
                },
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1"
                    }
                  }
                }
              }
            },
            "labels": [
              {
                "region": "JP",
                "value": "smoking_disclaimer"
              },
              {
                "region": "JP",
                "value": "pse_disclaimer"
              }
            ],
            "league": null,
            "mediaMetadata": {
              "activeAspectRatio": 1.78,
              "audioTracks": [
                {
                  "features": [
                    "dolby_20"
                  ],
                  "language": "ja",
                  "name": null,
                  "renditionName": "Japanese",
                  "trackType": "PRIMARY"
                }
              ],
              "captions": [
                {
                  "language": "zh-Hant",
                  "name": null,
                  "renditionName": "Chinese (Traditional)",
                  "trackType": "NORMAL"
                },
                {
                  "language": "ja",
                  "name": null,
                  "renditionName": "Japanese [CC]",
                  "trackType": "SDH"
                },
                {
                  "language": "en",
                  "name": null,
                  "renditionName": "English",
                  "trackType": "NORMAL"
                }
              ],
              "facets": [
                {
                  "activeAspectRatio": 1.78,
                  "label": "default"
                }
              ],
              "features": [
                "sdr",
                "hdr"
              ],
              "format": "HD",
              "mediaId": "3232bf83-75e6-40f0-9a29-dee51ec0605f",
              "phase": "active",
              "playbackUrls": [
                {
                  "rel": "video",
                  "href": "https://disney.playback.edge.bamgrid.com/media/3232bf83-75e6-40f0-9a29-dee51ec0605f/scenarios/{scenario}",
                  "templated": true,
                  "params": [
                    {
                      "name": "scenario",
                      "description": "Playback scenario"
                    }
                  ]
                }
              ],
              "productType": "VOD",
              "runtimeMillis": 1471000,
              "state": "ON",
              "type": "VIDEO"
            },
            "meta": null,
            "mediaRights": {
              "violations": [],
              "downloadBlocked": false,
              "pconBlocked": false,
              "rewind": true
            },
            "milestone": {
              "FFOC": [
                {
                  "id": "864251df-692e-4a98-a84d-55011e71081a",
                  "milestoneTime": [
                    {
                      "startMillis": 1001,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "intro_start": [
                {
                  "id": "48d1d519-66bd-477e-b2f5-fc293fb6a5a8",
                  "milestoneTime": [
                    {
                      "startMillis": 45045,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "FFEI": [
                {
                  "id": "4da79145-0796-4ed6-8dee-d496b2036483",
                  "milestoneTime": [
                    {
                      "startMillis": 45045,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "intro_end": [
                {
                  "id": "0695126d-b7a3-4684-9cec-e72dd29554be",
                  "milestoneTime": [
                    {
                      "startMillis": 135010,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "FFEC": [
                {
                  "id": "8c0874de-6a95-4891-844b-8503a699ed65",
                  "milestoneTime": [
                    {
                      "startMillis": 1370996,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "up_next": [
                {
                  "id": "0cc3233e-19ad-4870-a70e-ea23767a461c",
                  "milestoneTime": [
                    {
                      "startMillis": 1376001,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "LFEC": [
                {
                  "id": "35b811dc-3daa-4879-a6b6-6c5111b953bb",
                  "milestoneTime": [
                    {
                      "startMillis": 1460961,
                      "type": "offset"
                    }
                  ]
                }
              ],
              "LFOC": [
                {
                  "id": "e762c86a-64dd-47c1-b8b7-fe054e175af0",
                  "milestoneTime": [
                    {
                      "startMillis": 1470971,
                      "type": "offset"
                    }
                  ]
                }
              ]
            },
            "originalLanguage": "ja",
            "participant": {
              "Actor": [
                {
                  "characterDetails": {
                    "character": "フリーレン",
                    "characterId": "322795247"
                  },
                  "displayName": "Atsumi Tanezaki",
                  "order": 1,
                  "participantId": "86906036",
                  "sortName": "敦美, 種﨑"
                },
                {
                  "characterDetails": {
                    "character": "フェルン",
                    "characterId": "322795246"
                  },
                  "displayName": "Kana Ichinose",
                  "order": 2,
                  "participantId": "190908111",
                  "sortName": "加那, 市ノ瀬"
                },
                {
                  "characterDetails": {
                    "character": "シュタルク",
                    "characterId": "322795346"
                  },
                  "displayName": "Chiaki Kobayashi",
                  "order": 3,
                  "participantId": "193439222",
                  "sortName": "千晃, 小林"
                },
                {
                  "characterDetails": {
                    "character": "ヒンメル",
                    "characterId": "322818264"
                  },
                  "displayName": "Nobuhiko Okamoto",
                  "order": 4,
                  "participantId": "189507914",
                  "sortName": "信彦, 岡本"
                },
                {
                  "characterDetails": {
                    "character": "ハイター",
                    "characterId": "322818265"
                  },
                  "displayName": "Hiroki Tochi",
                  "order": 5,
                  "participantId": "23219",
                  "sortName": "宏樹, 東地"
                },
                {
                  "characterDetails": {
                    "character": "アイゼン",
                    "characterId": "322823042"
                  },
                  "displayName": "Youji Ueda",
                  "order": 6,
                  "participantId": "42663081",
                  "sortName": "燿司, 上田"
                }
              ]
            },
            "programId": "5f6ea159-96fc-4c4f-adda-55c7b111136a",
            "programType": "episode",
            "ratings": [
              {
                "advisories": [
                  "Violence-Some"
                ],
                "description": null,
                "filingNumber": null,
                "system": "Custom:DisneyPlus:APAC",
                "value": "12+"
              }
            ],
            "releases": [
              {
                "releaseDate": "2023-12-01",
                "releaseOrg": null,
                "releaseType": "original",
                "releaseYear": 2023,
                "territory": null
              }
            ],
            "seasonId": "1eed1274-c21f-43b4-8c1d-fdb0249e74af",
            "seasonSequenceNumber": 1,
            "seriesId": "985af96c-1678-4907-92ca-84880f812456",
            "seriesType": "standard",
            "sport": null,
            "tags": [
              {
                "displayName": null,
                "type": "titleEidr",
                "value": "18B6-63E0-DF5A-F92B-8DA0-A"
              },
              {
                "displayName": null,
                "type": "disneyPlusOriginal",
                "value": "false"
              }
            ],
            "targetLanguage": "ja",
            "text": {
              "description": {
                "medium": {
                  "program": {
                    "default": {
                      "content": "After Sein the priest joined the party, they arrived at Raad region. However, Fern and Stark are having a fight there. Turns out it was caused by Stark not preparing any gift for Fern's birthday. Sein tries to give some advice to both of them, but then Frieren calls out to him.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  },
                  "series": {
                    "default": {
                      "content": "Elven mage Frieren defeats Demon Lord with hero Himmel's party. 50 years later, she returns to find Himmel aged and dying. Realizing her detachment from humanity, Frieren embarks on a journey to understand mortal life, meeting diverse people and facing various challenges along the way.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  }
                },
                "full": {
                  "program": {
                    "default": {
                      "content": "After Sein the priest joined the party, they arrived at Raad region. However, Fern and Stark are having a fight there. Turns out it was caused by Stark not preparing any gift for Fern's birthday. Sein tries to give some advice to both of them, but then Frieren calls out to him.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  },
                  "series": {
                    "default": {
                      "content": "Watch the new episode now.\n\nSome flashing lights sequences or patterns may affect photosensitive viewers.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  }
                },
                "brief": {
                  "series": {
                    "default": {
                      "content": "Elven mage Frieren embarks on a journey to understand humanity's mortality in an era of peace.",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "Sein tries to advice Fern and Stark who just had a fight, but then Frieren calls out to him.",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                }
              },
              "title": {
                "full": {
                  "series": {
                    "default": {
                      "content": "Frieren: Beyond Journey's End",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "Privilege of the Young",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                },
                "slug": {
                  "series": {
                    "default": {
                      "content": "frieren-beyond-journeys-end",
                      "language": "en-GB",
                      "sourceEntity": "series"
                    }
                  },
                  "program": {
                    "default": {
                      "content": "privilege-of-the-young",
                      "language": "en-GB",
                      "sourceEntity": "program"
                    }
                  }
                }
              }
            },
            "type": "DmcVideo",
            "typedGenres": [],
            "videoArt": [],
            "videoId": "b26fb81a-b1d0-418b-9bc0-ff302171325f"
          },
          {
            "badging": null,
            "callToAction": null,
            "channel": null,
            "contentId": "e580e24b-cfd0-49f7-81ab-ccb7c8e8efe1",
            "contentType": "full",
            "currentAvailability": {
              "region": "JP",
              "kidsMode": false
            },
            "event": null,
            "encodedSeriesId": "1rlaH8IM0pkQ",
            "episodeNumber": null,
            "episodeSequenceNumber": 15,
            "episodeSeriesSequenceNumber": 15,
            "family": {
              "encodedFamilyId": "2j59BCtdbbgj",
              "familyId": "ZGlzbmV5b3JnOmRpc25leS5jb206cmFkYXI6NTIwODE0",
              "parent": true,
              "parentRef": {
                "encodedSeriesId": "1rlaH8IM0pkQ",
                "programId": "6ad9af4e-6272-4a54-bb74-8cb5eb032459",
                "seasonId": "1eed1274-c21f-43b4-8c1d-fdb0249e74af",
                "seriesId": "985af96c-1678-4907-92ca-84880f812456"
              },
              "sequenceNumber": null
            },
            "groups": [
              {
                "name": "Non-TWDC",
                "partnerGroupId": "401208",
                "type": "disneyPlusStorefrontSubBrand"
              },
              {
                "name": "Star",
                "partnerGroupId": "377148",
                "type": "disneyPlusStorefrontBrand"
              }
            ],
            "internalTitle": "Frieren: Beyond Journey's End - s1e15 - e580e24b-cfd0-49f7-81ab-ccb7c8e8efe1",
            "image": {
              "thumbnail": {
                "1.78": {
                  "program": {
                    "default": {
                      "masterId": "FC4A8579A8CFA2DF514C74F29BE4240D4812AE2188F84AF1D3321DEF11B4E790",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/FC4A8579A8CFA2DF514C74F29BE4240D4812AE2188F84AF1D3321DEF11B4E790"
                    }
                  }
                }
              },
              "title_treatment": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "BD389E7A5EF75EB8CFDAB05C134C97232D6F8C097D0C91C3518096BB56463910",
                      "masterWidth": 1920,
                      "masterHeight": 1080,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/BD389E7A5EF75EB8CFDAB05C134C97232D6F8C097D0C91C3518096BB56463910"
                    }
                  }
                }
              },
              "tile": {
                "0.71": {
                  "series": {
                    "default": {
                      "masterId": "77CC1FC69866834FEE4B724A07A163CA65825CB75736BD3589AF6FDA2B6A74EA",
                      "masterWidth": 2000,
                      "masterHeight": 2818,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/77CC1FC69866834FEE4B724A07A163CA65825CB75736BD3589AF6FDA2B6A74EA"
                    }
                  }
                },
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "1129698D299F194FED20FEDC826413E9F0FA5281613BC57E7E645B359B3D56C7",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/1129698D299F194FED20FEDC826413E9F0FA5281613BC57E7E645B359B3D56C7"
                    }
                  }
                },
                "1.33": {
                  "series": {
                    "default": {
                      "masterId": "9F23483E3484C1BF8A4641819F2B18A657747B64A2B4BD7414287B11D0386B99",
                      "masterWidth": 2880,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/9F23483E3484C1BF8A4641819F2B18A657747B64A2B4BD7414287B11D0386B99"
                    }
                  }
                }
              },
              "background_up_next": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "0A0DA7884203201B1A13F29F8A52CCF4059F5E1377A10A0DF79951A3BF5F6B2C",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/0A0DA7884203201B1A13F29F8A52CCF4059F5E1377A10A0DF79951A3BF5F6B2C"
                    }
                  }
                }
              },
              "title_treatment_centered": {
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "56A9C8DA09747B319C6C419244665A8828C3F59B3469DD98261F9079B8D90360",
                      "masterWidth": 1920,
                      "masterHeight": 1080,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/56A9C8DA09747B319C6C419244665A8828C3F59B3469DD98261F9079B8D90360"
                    }
                  }
                }
              },
              "background_details": {
                "1.33": {
                  "series": {
                    "default": {
                      "masterId": "687D2F30F2DE4D3A55889109547F0A6CA82BA371B6FB3F4D3641F2F67D2739A4",
                      "masterWidth": 2880,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/687D2F30F2DE4D3A55889109547F0A6CA82BA371B6FB3F4D3641F2F67D2739A4"
                    }
                  }
                },
                "1.78": {
                  "series": {
                    "default": {
                      "masterId": "5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1",
                      "masterWidth": 3840,
                      "masterHeight": 2160,
                      "url": "https://prod-ripcut-delivery.disney-plus.net/v1/variant/disney/5F65362B6B8A2B5C0FB3818D0920194C484F2C3DA90B089C99EA6994746819B1"
                    }
                  }
                }
              }
            },
            "labels": [
              {
                "region": "JP",
                "value": "smoking_disclaimer"
              },
              {
                "region": "JP",
                "value": "pse_disclaimer"
              }
            ]…"

 ```
</details>

注意地区不同id相同，而且一个地区的图片，在另外一个地区的网页html里也有，html都一样
参考： 
The Movie Database (TMDB)
https://www.themoviedb.org ›
[【教程向】如何获取Disney+中文简体海报和分集剧情简介【zh-CN】](https://www.themoviedb.org/tv/155226/discuss/62f73383a313b80084e67cbd?language=ar-IQ&page=2)

`disney.content.edge.bamgrid.com` 域名换成 `https://content.global.edge.bamgrid.com` 也行，参考 https://forum.kodi.tv/printthread.php?tid=353316&page=41 的 https://content.global.edge.bamgrid.com/svc/content/DmcSeriesBundle/version/3.3/region/GB/audience/false/maturity/1450/language/en-GB/encodedSeriesId/3RUQKboZV3FF


获取cookie ：
  
```
  
```

参考

import speedtest


test = speedtest.Speedtest()


print('Loading Server List ')
test.get_servers()
print('Choosing best Server')
best = test.get_best_server()  # ! en iyi
print(f"Found : {best['host']} located in {best['country']}")

print('Performing Download Test...')
download_results = test.download()


print('Performing Upload  Test...')
upload_results = test.upload()
ping_result = test.results.ping

print(f"Download speed: {download_results/1024/1024:.2f} Mbit/second ")
print(f"Upload speed: {upload_results/1024/1024:.2f} Mbit/second")
print(f"Ping : {ping_result:.2f}ms")

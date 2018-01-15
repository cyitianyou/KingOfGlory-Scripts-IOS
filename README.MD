& "python" -m pip install -r requirements.txt
& "python" -m pip install --pre facebook-wda
# 解锁keychain，以便可以正常的签名应用，
PASSWORD="replace-with-your-password"
security unlock-keychain -p $PASSWORD ~/Library/Keychains/login.keychain

# 获取设备的UDID
UDID=$(idevice_id -l | head -n1)

# 运行测试
xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=$UDID" test
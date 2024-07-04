## How to read a project
1. need to know the main arch/algorithm of this project
2. need to know the 4+1 view of this project
3. need to know how to run the test/example

内网网络原则
- 外网：设置代理
- 内网：需要排除（export no_proxy=*. huawei. com,*. tools. huawei. com, cmc-cd-mirror. rnd. huawei. com），否则报错 proxy 相关错

），否则
## How to set a project
#### Java
1. Maven编译指令
mvn clean install -DskipTests -Dscala-2.11 -Dmaven.javadoc.skip=true -Dcheckstyle.skip=true -Drat.skip=true -Dgit.commit.id.skip=true -T16
#### C++

#### python
pip内网设置

vi /etc/pip.conf
[global]
no-cache-dir = true
index-url = https://pypi.org/simple
extra-index-url = http://cmc-cd-mirror.rnd.huawei.com/pypi/simple/
trusted-host = cmc-cd-mirror.rnd.huawei.com
timeout = 2

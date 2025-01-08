[Git Submodules 介绍](https://cloud.tencent.com/developer/article/2136829)

Submodules 关键点：

1. submodules 的 git 库不感知它是哪些库的 sub modules
2. submodules 的修改会作为主项目的一部分，产生diff
3. 可以 cd  sub modules 进行子库的切换分支、提交代码、拉取更新
## git​

常用命令

git reflog 查看所有历史命令

git log --pretty=oneline 查看历史的commit

git reset --hard commit-id 强制将文件的修改回退到commit-id处，结合git reflog可以实现任意commit之间的切换

git revert commit-id : 可在idea上操作，通过提交一个新的commit来将原commit-id的内容删除掉

公司内部用ssh，不用https,以便 不用取消代理
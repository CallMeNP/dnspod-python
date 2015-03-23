# dnspod-python
DNSPod for python

修改了原 dnspod-python 库的domainRemove方法的参数，支持使用`domain`和`domain_id`两种方式

## 更新指定域名下的所有记录
```bash
python updateRecord.py -h
```
```
updateRecord.py usage:
-h,--help: print help message.
-v, --version: print script version
-d, --domain: 域名 
-r, --record-file: record file, 从 dnspod 客户端中导出
-e, --email: 帐号
-p, --password: 密码
```

记录文件使用dnspod客户端导出的txt文件。_请注意删除其中的NS记录_

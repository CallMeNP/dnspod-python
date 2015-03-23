#!/usr/bin/env python
# -*- coding:utf-8 -*-

from dnspod.apicn import *
import sys
import getopt


def updateRecord(domain, record_file, email, password):
    # 删除域名
    try:
        print "DomainRemove"
        api = DomainRemove(domain=domain, email=email, password=password)
        print api()
    except Exception as e:
        print e

    # 创建域名
    print "DomainCreate", domain
    api = DomainCreate(domain, email=email, password=password)

    domain_id = api().get("domain", {}).get("id")
    print "%s's id is %s" % (domain, domain_id)

    # 读取文件，解析，创建记录
    f = open(record_file)
    line = f.readline()
    while line:
        record_arr = line.split('\t')
        if len(record_arr) == 6:
            print ''
            print "RecordCreate"
            print record_arr
            api = RecordCreate(record_arr[0], record_arr[1], record_arr[2], record_arr[3], record_arr[5], domain_id=domain_id, email=email, password=password)
            record = api().get("record", {})
            record_id = record.get("id")
            print "Record id", record_id
        else:
            pass

        line = f.readline()
    f.close()


def main():
    domain = record_file = email = password = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hvd:r:e:p:', ['domain=', 'record-file=', 'email=', 'password='])
    except getopt.GetoptError, err:
        print str(err)
        Usage()
        sys.exit(2)
    for o, a in opts:
        if o in ('-h', '--help'):
            Usage()
            sys.exit(1)
        elif o in ('-v', '--version'):
            Version()
            sys.exit(0)
        elif o in ('-d', '--domain'):
            domain = a
        elif o in ('-r', '--record-file'):
            record_file = a
        elif o in ('-e', '--email'):
            email = a
        elif o in ('-p', '--password'):
            password = a
        else:
            print 'unhandled option: %s' % o
            Usage()
            sys.exit(3)
    if not domain or not record_file or not email or not password:
        Usage()
        sys.exit(1)
    updateRecord(domain, record_file, email, password)


def Usage():
    print '%s usage:' % sys.argv[0]
    print '-h,--help: print help message.'
    print '-v, --version: print script version'
    print '-d, --domain: 域名 '
    print '-r, --record-file: record file, 从 dnspod 客户端中导出'
    print '-e, --email: 帐号'
    print '-p, --password: 密码'


def Version():
    print '%s 1.0.0.0.1' % sys.argv[0]


if __name__ == '__main__':
    main()

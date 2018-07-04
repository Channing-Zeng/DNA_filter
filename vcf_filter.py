#!usr/bin/python 3

f1=open('d:/CHG029162.ready.snp.vcf','r')
f2=open('d:/vcf1.txt','w')
list2=[]

for i in f1:
    list1=i.split(':')
    if ('chrY' in i) and ('PASS' in i) and int(list1[6])>=100:
        list2.append(i)

    
f2.writelines(list2)
f2.close()



###f1=open('/oline/home/zengql/vcf/CHG029161.vcf','r')
###f2=open('/oline/home/zengql/vcf/vcf1.txt','w')

#END

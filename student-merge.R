d1=read.table("/Users/mac/Downloads/student/student-por.csv",sep=";",header=TRUE)
d2=read.table("/Users/mac/Downloads/student/student-por.csv",sep=";",header=TRUE)

d3=merge(d1,d2,by=c("school","sex","age","address","famsize","Pstatus","Medu","Fedu","Mjob","Fjob","reason","nursery","internet"))
print(nrow(d3)) # 382 students

write.csv(d3, file = "/Users/mac/Downloads/student/student.csv")
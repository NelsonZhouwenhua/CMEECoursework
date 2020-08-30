library(ape)
library(phytools)
require(reshape2)
library(factoextra)
setwd("~/PycharmProjects/MRes_project")

# read trees and tree sequences and draw consensus trees
tree.asp <- read.tree("testnewick.txt")
date.tree <- read.tree(file =  "datenewick.txt")

tree.MT <- read.tree("MT_infer.txt")
tree.MTdate <- read.tree(file =  "MT_date_1.txt")
tree.IIdate <- read.tree(file =  "II_date.txt")
tree.IIIdate <- read.tree(file =  "III_date.txt")
tree.IVdate <- read.tree(file =  "IV_date.txt")
tree.Vdate <- read.tree(file =  "V_date.txt")
tree.VIdate <- read.tree(file =  "VI_date.txt")
tree.VIIdate <- read.tree(file =  "VII_date.txt")
tree.VIIIdate <- read.tree(file =  "VIII_date.txt")
#kronoviz(tree.asp, layout = 100)

#my.contree1<-consensus(tree.asp,p=1)
#plot(my.contree1)
MT.contree1<-consensus(tree.MT,p=1)
MTdate.contree1<-consensus(tree.MTdate,p=1)
I.contree1 <- consensus(tree.asp,p=1)
Idate.contree1 <- consensus(date.tree, p=1)
II.contree1 <- consensus(tree.IIdate,p=1)
III.contree1 <- consensus(tree.IIIdate,p=1)
IV.contree1 <- consensus(tree.IVdate,p=1)
V.contree1 <- consensus(tree.Vdate,p=1)
VI.contree1 <- consensus(tree.VIdate,p=1)
VII.contree1 <- consensus(tree.VIIdate,p=1)
VIII.contree1 <- consensus(tree.VIIIdate,p=1)


#my.contree2<-consensus(tree.asp,p=0.5)
#plot(my.contree2)
MT.contree2<-consensus(tree.MT,p=0.5)
MTdate.contree2<-consensus(tree.MTdate,p=0.5)
I.contree2 <- consensus(tree.asp,p=0.5)
Idate.contree2 <- consensus(date.tree, p=0.5)
II.contree2 <- consensus(tree.IIdate,p=0.5)
III.contree2 <- consensus(tree.IIIdate,p=0.5)
IV.contree2 <- consensus(tree.IVdate,p=0.5)
V.contree2 <- consensus(tree.Vdate,p=0.5)
VI.contree2 <- consensus(tree.VIdate,p=0.5)
VII.contree2 <- consensus(tree.VIIdate,p=0.5)
VIII.contree2 <- consensus(tree.VIIIdate,p=0.5)

plotTree(I.contree2,type="fan",ftype="i",fsize=0.6,lwd=1)
plotTree(Idate.contree2,type="fan",ftype="i",fsize=0.6,lwd=1)
plotTree(MT.contree2,type="fan",ftype="i",fsize=0.6,lwd=1)
plotTree(MTdate.contree2,type="fan",ftype="i",fsize=0.6,lwd=1)
plotTree(II.contree2,type="fan",ftype="i",fsize=0.6,lwd=1)
plotTree(III.contree2,type="fan",ftype="i",fsize=0.6,lwd=1)
plotTree(IV.contree2,type="fan",ftype="i",fsize=0.6,lwd=1)
plotTree(V.contree2,type="fan",ftype="i",fsize=0.6,lwd=1)
plotTree(VI.contree2,type="fan",ftype="i",fsize=0.6,lwd=1)
plotTree(VII.contree2,type="fan",ftype="i",fsize=0.6,lwd=1)
plotTree(VIII.contree2,type="fan",ftype="i",fsize=0.6,lwd=1)

fasttree <- read.tree("data/tree.txt")
plotTree(fasttree,type="fan",ftype="i",fsize=0.3,lwd=1)
fasttree.I <- read.tree("data/I.txt")
plotTree(fasttree.I,type="fan",ftype="i",fsize=0.6,lwd=1)

# GNN methods
dat <- data.matrix(read.csv("GNN.csv", header = FALSE,sep = ","))
gnn <- round(dat,3)
nodelabels <- c('ARAF001','ARAF002','ARAF003','ARAF004','ARAF005','ARAF006','C1','C10','C100','C103','C104',
                'C105','C106','C107','C108','C109','C11','C110','C111','C112','C113',
                'C114','C115','C116','C117','C118','C119','C12','C120','C121','C122',
                'C123','C124','C125','C126','C127','C128','C129','C13','C130','C131',
                'C132','C133','C134','C135','C136','C137','C138','C139','C14','C140',
                'C141','C142','C143','C144','C145','C146','C147','C148','C149','C15', 
                'C150','C151','C152','C153','C154','C155','C156','C157','C158','C159',
                'C16','C160','C161','C162','C163','C164','C165','C166','C167','C168', 
                'C169','C17','C170','C171','C172','C173','C174','C175','C176','C177',
                'C178','C179','C18','C180','C181','C182','C183','C184','C185','C186',
                'C187','C188','C189','C19','C190','C191','C2','C20','C21','C22',
                'C220','C221','C222','C223','C23','C24','C246','C25','C26','C27',
                'C272','C275','C28','C29','C3','C30','C31','C32','C33','C34',
                'C341','C342','C343','C344','C345','C346','C35','C354','C355','C356',
                'C357','C358','C359','C36','C360','C361','C362','C363','C364','C365',
                'C366','C367','C368','C369','C37','C38','C39','C4','C40','C41',
                'C42','C43','C44','C45','C46','C47','C48','C49','C5','C50',
                'C51','C52','C53','C54','C55','C56','C57','C58','C59','C6',
                'C60','C61','C62','C63','C64','C65','C66','C67','C68','C69',
                'C7','C70','C71','C72','C73','C74','C75','C76','C77','C78',
                'C79','C8','C80','C81','C82','C83','C84','C85','C86','C87',
                'C88','C89','C91','C92','C93','C95','C96','C99')
colnames(gnn) <- nodelabels
rownames(gnn) <- nodelabels

# select nodes heatmap
rm.col <- c()
for (i in 1:length(gnn[1,])){
  if (max(gnn[i,])>0.2){
    rm.col <- c(rm.col,i)
  }
}
rm.col
gnn.select <- gnn[rm.col,rm.col]
a <- gnn.select[-18,-18]
a <- a[c(1,8,2,20,30,3,29,4,5,7,14,17,6,9,15,10,11,12,13,16,22,26,18,19,21,27,23,24,25,28),c(1,8,2,20,30,3,29,4,5,7,14,17,6,9,15,10,11,12,13,16,22,26,18,19,21,27,23,24,25,28)]
a <- as.dist(a)
fviz_dist(a, lab_size = 8,order = FALSE,gradient = list(low = "black", mid = "white", high = "blue"))

# full nodes heatmap
b <- as.dist(gnn)
fviz_dist(b, lab_size = 8,order = FALSE,gradient = list(low = "black", mid = "white", high = "blue"))


#phylo.heatmap(MTdate.contree2,X,standardize=TRUE)

#write.tree(MTdate.contree2,file = "MTdate.txt")


import pandas as px 
import  csv
import plotly.figure_factory as ff
import statistics
df=px.read_csv("performa.csv")
writings=df["writing"].to_list()
meanw=statistics.mean( writings)
medianw=statistics.median(writings)
modew=statistics.mode(writings)
sdw=statistics.stdev(writings)
print(meanw)
print(medianw)
print(modew)
print(sdw)
figure=ff.create_distplot([df["writing"].tolist()],["writing"],show_hist=False)
fsdstart,fsdend=meanw-sdw,meanw+sdw
secsdstart,secsdstartend=meanw-(2*sdw),meanw+(2*sdw)
thsdstart,thsdstartend=meanw(3*sdw),meanw+(3*sdw)


#printingvalues
datafsd=[result for result in writings if result>fsdstart<fsdend]
datassd=[result for result in writings if result>secsdstart<secsdstartend]
datathsd=[result for result in writings if result>thsdstart<thsdstartend]
print("{}% datalies within fsd ".format(len(datafsd)*100/len( writings)))
print("{}% datalies within ssd".format(len(datassd)*100/len( writings)))
print("{}% datalies within thsd".format(len(datathsd)*100/len( writings)))

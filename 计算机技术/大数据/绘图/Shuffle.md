---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
sortShuffle ^dhw2DzKA

BypassMergeSortShuffleWriter
与优化后的hashshuffle区别在于
hashshuffle合并mapper task到一个文件，便于reducer拉取
Bypass合并reducer 所需文件到一个文件，提供index
 ^sbquvKrx

1.这里其实只有一个内存buffer
2.why when reducer become bigger prefer using sortshuffle
sortshuffle只需开一个buffer，而bypass需要为每个分区开一个buffer,
因而一方面占用内存（32KB each partition），更重要的是持有太多文件句柄 ^zATQgjeO

sortshuffle只需开一个buffer，而bypass需要为每个分区开一个buffer ^Wl0WMcKy

Pt1 buffer
address list ^ss7mnIys

Pt2 
address list ^yEQBlUBQ

pt1 buffer
4096 rows ^NPmy1VTC

pt1 buffer ^dQI20SQX

满一定大小后（2GB），
进行序列化、
压缩spill ^2ADQjYT7

pt buffer list ^8rFGr3eC

buffer 满了
申请新buffer ^VzZypjhL

vector batch ^grQz5EwG

 Temp File ^MdapwiCt

Temp File ^w6Iq9SnH

output file ^fPQXoKrV

vector batch ^9t8P9BGS

Task ^NRlF12hV

merge ^vx5PT4yf

partition ^usiFav72

OmniRuntime native shuffle
占用大量内存，但无需持有多个文件句柄 ^RW60pcrQ

map*reduce*executor个小文件 ^3dskBaTI

reducer*executor个文件 ^ZGSHiltx

executor*Reducer个文件 ^9eNW8JbL

executor*Reducer个文件 ^MprMud7S

BypassMergeSortShuffle ^JZPAgToH

[[Spark Native列式Shuffle.pptx]] ^de9w8rht

spark.shuffle.file.buffer=32k ^vU3AdB1g

当前Omni shuffle的实现与bypass几乎一样，除了spark.shuffle.file.buffer设置为了2GB，
因而减少了生成的文件
问题：
1. 没有一直持有文件句柄，因而一个分区可能会生成多个小文件，
而bypass一直持有，一个分区对应一个文件
2.当前的buffer内存未被统计，executor offheap memory中，
当一个节点运行多个task时，可能存在大量未被统计的内存使用，
如典配下：96核*2GB=192GB内存未被统计，导致杀进程 ^engw6p6o

1630 没有12大盘场景；
7270 920b 64核
 ^CauKfj2d


# Embedded files
69f6f24a0fa0c19dbe15ad7772ce084bf2cf4962: [[attachments/Pasted Image 20230720171854_105.png]]
61e3b5d1dcab773f8a06e7c3f274197bd9781a06: [[attachments/Pasted Image 20230720171926_435.png]]
2294e30e28dbf90805d6bf631887d157930f87b8: [[attachments/Pasted Image 20230720171956_461.png]]
12d401376e1e0b86ed2a98b77185be95a309d658: [[attachments/Pasted Image 20230720172033_511.png]]
4f9553304cce93389e2065b89f5963a9296ecaac: [[attachments/Pasted Image 20230720195852_455.png]]
45645fedb59c90cd58a4b5e1a5ec32ce17cc6336: [[attachments/Pasted Image 20231106201456_908.png]]

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.0.4",
	"elements": [
		{
			"type": "rectangle",
			"version": 150,
			"versionNonce": 461317942,
			"isDeleted": false,
			"id": "H8yEu0pu4GrPJmq1-tPlU",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -17.920159900242766,
			"y": 1311.4356363718434,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 596.8421052631577,
			"height": 167.36842105263148,
			"seed": 423910166,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "7LcR-NauLucK90nvuufcG",
					"type": "arrow"
				}
			],
			"updated": 1699273156022,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 275,
			"versionNonce": 1020432170,
			"isDeleted": false,
			"id": "ZweovvZ4paPJxhQTPCqjF",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 67.00089273133602,
			"y": 1380.5935311086855,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 199.15789473684208,
			"height": 88.26315789473685,
			"seed": 1063128406,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false
		},
		{
			"type": "image",
			"version": 381,
			"versionNonce": 448843894,
			"isDeleted": false,
			"id": "lYSBIjGjyS7MGP7cXtLcw",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -990.5834420313486,
			"y": -1007.9423742943741,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 791.0518870857657,
			"height": 431.62871729426155,
			"seed": 1114616458,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "69f6f24a0fa0c19dbe15ad7772ce084bf2cf4962",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "image",
			"version": 380,
			"versionNonce": 181082602,
			"isDeleted": false,
			"id": "1UefjjDF8lcJ7dKX0bOgM",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -939.5919634270673,
			"y": -560.6180672803212,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 762.3876800034509,
			"height": 431.62871729426143,
			"seed": 404164234,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "61e3b5d1dcab773f8a06e7c3f274197bd9781a06",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "image",
			"version": 327,
			"versionNonce": 779833782,
			"isDeleted": false,
			"id": "LrN_ZPgrHrixwvcgaxoCo",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -941.8027099863318,
			"y": -119.83358931618133,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 769.4251047419446,
			"height": 431.62871729426155,
			"seed": 1862997130,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "2294e30e28dbf90805d6bf631887d157930f87b8",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "text",
			"version": 858,
			"versionNonce": 1398032539,
			"isDeleted": false,
			"id": "sbquvKrx",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1501.6069653844509,
			"y": 1176.86920571755,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 645.9320068359375,
			"height": 151.7632675977763,
			"seed": 1975430422,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699323680491,
			"link": null,
			"locked": false,
			"fontSize": 25.293877932962715,
			"fontFamily": 4,
			"text": "BypassMergeSortShuffleWriter\n与优化后的hashshuffle区别在于\nhashshuffle合并mapper task到一个文件，便于reducer拉取\nBypass合并reducer 所需文件到一个文件，提供index\n",
			"rawText": "BypassMergeSortShuffleWriter\n与优化后的hashshuffle区别在于\nhashshuffle合并mapper task到一个文件，便于reducer拉取\nBypass合并reducer 所需文件到一个文件，提供index\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "BypassMergeSortShuffleWriter\n与优化后的hashshuffle区别在于\nhashshuffle合并mapper task到一个文件，便于reducer拉取\nBypass合并reducer 所需文件到一个文件，提供index\n",
			"lineHeight": 1.2,
			"baseline": 145
		},
		{
			"type": "text",
			"version": 330,
			"versionNonce": 485432294,
			"isDeleted": false,
			"id": "zATQgjeO",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -120.57564366076417,
			"y": 620.7886793613928,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 857.45849609375,
			"height": 121.26315789473676,
			"seed": 1020426710,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "dQNJ3rkcmTTAKGhACn0ZV",
					"type": "arrow"
				}
			],
			"updated": 1706323522203,
			"link": null,
			"locked": false,
			"fontSize": 25.26315789473683,
			"fontFamily": 4,
			"text": "1.这里其实只有一个内存buffer\n2.why when reducer become bigger prefer using sortshuffle\nsortshuffle只需开一个buffer，而bypass需要为每个分区开一个buffer,\n因而一方面占用内存（32KB each partition），更重要的是持有太多文件句柄",
			"rawText": "1.这里其实只有一个内存buffer\n2.why when reducer become bigger prefer using sortshuffle\nsortshuffle只需开一个buffer，而bypass需要为每个分区开一个buffer,\n因而一方面占用内存（32KB each partition），更重要的是持有太多文件句柄",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "1.这里其实只有一个内存buffer\n2.why when reducer become bigger prefer using sortshuffle\nsortshuffle只需开一个buffer，而bypass需要为每个分区开一个buffer,\n因而一方面占用内存（32KB each partition），更重要的是持有太多文件句柄",
			"lineHeight": 1.2,
			"baseline": 115
		},
		{
			"type": "embeddable",
			"version": 88,
			"versionNonce": 1258271615,
			"isDeleted": false,
			"id": "VB2HOsuD_WHVo9SrjfaEa",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 71.91342933875399,
			"y": -639.7188196249416,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 560,
			"height": 840,
			"seed": 954535958,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1707208495177,
			"link": "https://medium.com/@philipp.brunenberg/understanding-apache-spark-hash-shuffle-b9aed2d587b0",
			"locked": false,
			"validated": true,
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 80,
			"versionNonce": 323935286,
			"isDeleted": false,
			"id": "RRuSFIIYJTjtc4J48l8Yp",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1237.9300989462065,
			"y": 613.5404158070389,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 151,
			"height": 135,
			"seed": 1464225814,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "tdhpmyk1w6ZHjFgI5tb-L",
					"type": "arrow"
				},
				{
					"id": "yLA_Bww1lYOWEG7R_T17A",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "Wl0WMcKy"
				}
			],
			"updated": 1699273156023,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 288,
			"versionNonce": 2050356602,
			"isDeleted": false,
			"id": "Wl0WMcKy",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1232.4300989462065,
			"y": 621.0404158070389,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 140,
			"height": 120,
			"seed": 548696534,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703034079548,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "sortshuffle只\n需开一个buffer\n，而bypass需要\n为每个分区开一\n个buffer",
			"rawText": "sortshuffle只需开一个buffer，而bypass需要为每个分区开一个buffer",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "RRuSFIIYJTjtc4J48l8Yp",
			"originalText": "sortshuffle只需开一个buffer，而bypass需要为每个分区开一个buffer",
			"lineHeight": 1.2,
			"baseline": 115
		},
		{
			"type": "arrow",
			"version": 897,
			"versionNonce": 791150513,
			"isDeleted": false,
			"id": "tdhpmyk1w6ZHjFgI5tb-L",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -916.5583496384436,
			"y": 565.9403815449526,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 166.8041091212947,
			"height": 53.88084228058767,
			"seed": 1118011990,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1707208495305,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "HJLQ2rrhKtNMOE3a41pzl",
				"gap": 20.4868556255243,
				"focus": 0.5153895674817747
			},
			"endBinding": {
				"elementId": "RRuSFIIYJTjtc4J48l8Yp",
				"gap": 3.567640186468225,
				"focus": -0.3882868556772639
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-166.8041091212947,
					53.88084228058767
				]
			]
		},
		{
			"type": "arrow",
			"version": 1268,
			"versionNonce": 1308526449,
			"isDeleted": false,
			"id": "yLA_Bww1lYOWEG7R_T17A",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -854.9667662420766,
			"y": 1040.6032301008036,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 230.5056749397679,
			"height": 327.8562815728253,
			"seed": 25950422,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1707208495306,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Yen04XoJ44Tck3K_NhQc3",
				"gap": 8.562449326358546,
				"focus": -0.42754349407923253
			},
			"endBinding": {
				"elementId": "RRuSFIIYJTjtc4J48l8Yp",
				"gap": 1.4576577643620112,
				"focus": -0.4445919396803446
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-230.5056749397679,
					-327.8562815728253
				]
			]
		},
		{
			"type": "rectangle",
			"version": 160,
			"versionNonce": 60933814,
			"isDeleted": false,
			"id": "DALM_EuqnZjUNpc7BxYaB",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 38.92194536291481,
			"y": 1341.4093205823701,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffc9c9",
			"width": 196,
			"height": 83,
			"seed": 727791126,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "NPmy1VTC"
				},
				{
					"id": "L2PGgG5dHo1QgEU0A45sC",
					"type": "arrow"
				},
				{
					"id": "Whbq0M-5PoxYZ2Huve9Au",
					"type": "arrow"
				}
			],
			"updated": 1699273156023,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 190,
			"versionNonce": 1431021482,
			"isDeleted": false,
			"id": "NPmy1VTC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 92.33210161291481,
			"y": 1358.9093205823701,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 89.1796875,
			"height": 48,
			"seed": 1773465994,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "pt1 buffer\n4096 rows",
			"rawText": "pt1 buffer\n4096 rows",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "DALM_EuqnZjUNpc7BxYaB",
			"originalText": "pt1 buffer\n4096 rows",
			"lineHeight": 1.2,
			"baseline": 43
		},
		{
			"type": "rectangle",
			"version": 216,
			"versionNonce": 878936054,
			"isDeleted": false,
			"id": "vJvGV98mYjoDRY2-D3fWy",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 143.23773483659897,
			"y": 1183.9619521613172,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 550.5263157894733,
			"height": 82.10526315789502,
			"seed": 190003082,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 98,
			"versionNonce": 1435312746,
			"isDeleted": false,
			"id": "Z5Lz88gJO0Z36mcOZzwae",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 259.0272085208097,
			"y": 1183.9619521613167,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 81.05263157894728,
			"seed": 1607302282,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0,
					81.05263157894728
				]
			]
		},
		{
			"type": "line",
			"version": 116,
			"versionNonce": 1864110390,
			"isDeleted": false,
			"id": "oiP38NmNSgPRgfwWrgjgk",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 364.81302974408607,
			"y": 1183.7320287504344,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 81.05263157894728,
			"seed": 1606859978,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0,
					81.05263157894728
				]
			]
		},
		{
			"type": "line",
			"version": 108,
			"versionNonce": 760300842,
			"isDeleted": false,
			"id": "K7zCWmjjLhn5Ymw7EsX7U",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 469.02355605987543,
			"y": 1186.889923487277,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 0,
			"height": 81.05263157894728,
			"seed": 1955801162,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": null,
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": null,
			"points": [
				[
					0,
					0
				],
				[
					0,
					81.05263157894728
				]
			]
		},
		{
			"type": "text",
			"version": 180,
			"versionNonce": 144080187,
			"isDeleted": false,
			"id": "ss7mnIys",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 157.97457694186232,
			"y": 1202.9093205823692,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 86.54338073730469,
			"height": 37.8947368421052,
			"seed": 310941578,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "L2PGgG5dHo1QgEU0A45sC",
					"type": "arrow"
				}
			],
			"updated": 1699323680493,
			"link": null,
			"locked": false,
			"fontSize": 15.7894736842105,
			"fontFamily": 4,
			"text": "Pt1 buffer\naddress list",
			"rawText": "Pt1 buffer\naddress list",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Pt1 buffer\naddress list",
			"lineHeight": 1.2,
			"baseline": 34
		},
		{
			"type": "text",
			"version": 208,
			"versionNonce": 1342654453,
			"isDeleted": false,
			"id": "yEQBlUBQ",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 267.7798868398372,
			"y": 1206.3303732139484,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 91.64381408691406,
			"height": 40.10871110788606,
			"seed": 931649610,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "izPh5encIbKc-3iHDP0sr",
					"type": "arrow"
				}
			],
			"updated": 1699323680495,
			"link": null,
			"locked": false,
			"fontSize": 16.711962961619193,
			"fontFamily": 4,
			"text": "Pt2 \naddress list",
			"rawText": "Pt2 \naddress list",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Pt2 \naddress list",
			"lineHeight": 1.2,
			"baseline": 36
		},
		{
			"type": "arrow",
			"version": 423,
			"versionNonce": 589700913,
			"isDeleted": false,
			"id": "L2PGgG5dHo1QgEU0A45sC",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 125.09541223027404,
			"y": 1335.5408995297375,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 67.72496948646281,
			"height": 91.57894736842081,
			"seed": 789822358,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1707208495309,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "DALM_EuqnZjUNpc7BxYaB",
				"gap": 5.868421052632584,
				"focus": -0.36410425901095306
			},
			"endBinding": {
				"elementId": "ss7mnIys",
				"gap": 3.1578947368424224,
				"focus": -0.13828564673620597
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					67.72496948646281,
					-91.57894736842081
				]
			]
		},
		{
			"type": "rectangle",
			"version": 279,
			"versionNonce": 598573738,
			"isDeleted": false,
			"id": "-iPbTJESz2Q6XjR58ss9f",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 298.2245769418623,
			"y": 1368.8961626876326,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 196,
			"height": 83,
			"seed": 934786326,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 192,
			"versionNonce": 1507906806,
			"isDeleted": false,
			"id": "ZOEQ0tH1iR0da3GpL6XIE",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 280.6719453629148,
			"y": 1347.6066890034226,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffc9c9",
			"width": 196,
			"height": 83,
			"seed": 543990358,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "dQI20SQX"
				},
				{
					"id": "izPh5encIbKc-3iHDP0sr",
					"type": "arrow"
				},
				{
					"id": "77vY-qNkLkLwBM2o2HzhQ",
					"type": "arrow"
				}
			],
			"updated": 1699273156023,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 210,
			"versionNonce": 1358667114,
			"isDeleted": false,
			"id": "dQI20SQX",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 334.0821016129148,
			"y": 1377.1066890034226,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 89.1796875,
			"height": 24,
			"seed": 378660758,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "pt1 buffer",
			"rawText": "pt1 buffer",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "ZOEQ0tH1iR0da3GpL6XIE",
			"originalText": "pt1 buffer",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "arrow",
			"version": 362,
			"versionNonce": 223903409,
			"isDeleted": false,
			"id": "izPh5encIbKc-3iHDP0sr",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 362.32745846221434,
			"y": 1342.9093205823692,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 53.95188581721669,
			"height": 81.99655205000818,
			"seed": 34003466,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1707208495311,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "ZOEQ0tH1iR0da3GpL6XIE",
				"gap": 4.6973684210533975,
				"focus": 0.11214414626589472
			},
			"endBinding": {
				"elementId": "yEQBlUBQ",
				"gap": 14.473684210526585,
				"focus": 0.4735040641783037
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-53.95188581721669,
					-81.99655205000818
				]
			]
		},
		{
			"type": "text",
			"version": 331,
			"versionNonce": 216604123,
			"isDeleted": false,
			"id": "2ADQjYT7",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 588.0047740587256,
			"y": 1315.9128051636405,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 209.765625,
			"height": 72,
			"seed": 1762428426,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699323680496,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "满一定大小后（2GB），\n进行序列化、\n压缩spill",
			"rawText": "满一定大小后（2GB），\n进行序列化、\n压缩spill",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "满一定大小后（2GB），\n进行序列化、\n压缩spill",
			"lineHeight": 1.2,
			"baseline": 67
		},
		{
			"type": "text",
			"version": 172,
			"versionNonce": 1747222869,
			"isDeleted": false,
			"id": "8rFGr3eC",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 345.34299799449366,
			"y": 1150.2777416350013,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 125.8984375,
			"height": 24,
			"seed": 1369998154,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699323680496,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "pt buffer list",
			"rawText": "pt buffer list",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "pt buffer list",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "text",
			"version": 266,
			"versionNonce": 2069801595,
			"isDeleted": false,
			"id": "VzZypjhL",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 127.4482611523888,
			"y": 1428.1724784771063,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 81.48802185058594,
			"height": 33.85263157894764,
			"seed": 1235301526,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699323680498,
			"link": null,
			"locked": false,
			"fontSize": 14.10526315789485,
			"fontFamily": 4,
			"text": "buffer 满了\n申请新buffer",
			"rawText": "buffer 满了\n申请新buffer",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "buffer 满了\n申请新buffer",
			"lineHeight": 1.2,
			"baseline": 30
		},
		{
			"type": "rectangle",
			"version": 326,
			"versionNonce": 453456054,
			"isDeleted": false,
			"id": "75c51V2QzEAqv7Srgx6za",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 105.92194536291532,
			"y": 1607.6198468981588,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 322,
			"height": 59,
			"seed": 2016573770,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "grQz5EwG"
				},
				{
					"id": "Whbq0M-5PoxYZ2Huve9Au",
					"type": "arrow"
				},
				{
					"id": "77vY-qNkLkLwBM2o2HzhQ",
					"type": "arrow"
				}
			],
			"updated": 1699273156023,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 165,
			"versionNonce": 1623842218,
			"isDeleted": false,
			"id": "grQz5EwG",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 211.43366411291532,
			"y": 1625.1198468981588,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 110.9765625,
			"height": 24,
			"seed": 836778826,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "vector batch",
			"rawText": "vector batch",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "75c51V2QzEAqv7Srgx6za",
			"originalText": "vector batch",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "arrow",
			"version": 581,
			"versionNonce": 295640625,
			"isDeleted": false,
			"id": "Whbq0M-5PoxYZ2Huve9Au",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 260.0798400997573,
			"y": 1600.804057424475,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 24.157894736842394,
			"height": 194.31350114416819,
			"seed": 721688586,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1707208495314,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "75c51V2QzEAqv7Srgx6za",
				"gap": 6.815789473683708,
				"focus": -0.014132529610501564
			},
			"endBinding": {
				"elementId": "DALM_EuqnZjUNpc7BxYaB",
				"gap": 1.0000000000000568,
				"focus": -0.9312600057086888
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-24.157894736842394,
					-194.31350114416819
				]
			]
		},
		{
			"type": "arrow",
			"version": 501,
			"versionNonce": 1864369649,
			"isDeleted": false,
			"id": "77vY-qNkLkLwBM2o2HzhQ",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 375.86931378396787,
			"y": 1603.9619521613167,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.631578947368325,
			"height": 170.52631578947353,
			"seed": 1976523350,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1707208495314,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "75c51V2QzEAqv7Srgx6za",
				"gap": 3.6578947368420813,
				"focus": 0.6525790190410203
			},
			"endBinding": {
				"elementId": "ZOEQ0tH1iR0da3GpL6XIE",
				"gap": 2.828947368420586,
				"focus": -0.12973230988795087
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					12.631578947368325,
					-170.52631578947353
				]
			]
		},
		{
			"type": "rectangle",
			"version": 429,
			"versionNonce": 128908086,
			"isDeleted": false,
			"id": "R2U3VydDkTMdNIKw3EsHS",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 752.8956295734416,
			"y": 1336.7251100560538,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 141,
			"height": 107,
			"seed": 306642506,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "7LcR-NauLucK90nvuufcG",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "MdapwiCt"
				},
				{
					"id": "pjtODo5pl-owDTxml6xKf",
					"type": "arrow"
				}
			],
			"updated": 1699273156023,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 252,
			"versionNonce": 1262091050,
			"isDeleted": false,
			"id": "MdapwiCt",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 777.8292233234416,
			"y": 1378.2251100560538,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 91.1328125,
			"height": 24,
			"seed": 1975429846,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": " Temp File",
			"rawText": " Temp File",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "R2U3VydDkTMdNIKw3EsHS",
			"originalText": " Temp File",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "arrow",
			"version": 780,
			"versionNonce": 1675230641,
			"isDeleted": false,
			"id": "7LcR-NauLucK90nvuufcG",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 579.9764252634536,
			"y": 1394.4927426512882,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 165.70316600757235,
			"height": 1.7875671036313179,
			"seed": 57066646,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1707208495316,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "H8yEu0pu4GrPJmq1-tPlU",
				"gap": 1.054479900538695,
				"focus": 0.02995929654047777
			},
			"endBinding": {
				"elementId": "R2U3VydDkTMdNIKw3EsHS",
				"gap": 7.2160383024156545,
				"focus": -0.030255560893615255
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					165.70316600757235,
					-1.7875671036313179
				]
			]
		},
		{
			"type": "rectangle",
			"version": 550,
			"versionNonce": 828704234,
			"isDeleted": false,
			"id": "jjc6fJ0OfMgPy2Z4CXlUy",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 756.9482611523895,
			"y": 1474.6724784771068,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 141,
			"height": 107,
			"seed": 1860924682,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "w6Iq9SnH"
				},
				{
					"id": "RT0iWn0hXhSYb49iOzYI5",
					"type": "arrow"
				}
			],
			"updated": 1699273156023,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 372,
			"versionNonce": 1204168118,
			"isDeleted": false,
			"id": "w6Iq9SnH",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 785.7881049023895,
			"y": 1516.1724784771068,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 83.3203125,
			"height": 24,
			"seed": 948716490,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "Temp File",
			"rawText": "Temp File",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "jjc6fJ0OfMgPy2Z4CXlUy",
			"originalText": "Temp File",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "rectangle",
			"version": 570,
			"versionNonce": 459323562,
			"isDeleted": false,
			"id": "miGWRGi71Z0Hur-egiOYE",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1000.1061558892311,
			"y": 1387.304057424475,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 239,
			"height": 99,
			"seed": 1824147274,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "fPQXoKrV"
				},
				{
					"id": "pjtODo5pl-owDTxml6xKf",
					"type": "arrow"
				},
				{
					"id": "RT0iWn0hXhSYb49iOzYI5",
					"type": "arrow"
				}
			],
			"updated": 1699273156023,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 397,
			"versionNonce": 1386479350,
			"isDeleted": false,
			"id": "fPQXoKrV",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 1068.785843389231,
			"y": 1424.804057424475,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 101.640625,
			"height": 24,
			"seed": 826723850,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "output file",
			"rawText": "output file",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "miGWRGi71Z0Hur-egiOYE",
			"originalText": "output file",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "arrow",
			"version": 506,
			"versionNonce": 550045041,
			"isDeleted": false,
			"id": "pjtODo5pl-owDTxml6xKf",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 897.1851032576516,
			"y": 1372.5860030474428,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 90.16687136487133,
			"height": 53.53432001882038,
			"seed": 1742750166,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1707208495316,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "R2U3VydDkTMdNIKw3EsHS",
				"gap": 3.289473684209952,
				"focus": -0.6444137900855851
			},
			"endBinding": {
				"elementId": "vx5PT4yf",
				"gap": 13.55674342105192,
				"focus": 1.6973287403773636
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					90.16687136487133,
					53.53432001882038
				]
			]
		},
		{
			"type": "arrow",
			"version": 710,
			"versionNonce": 1206459697,
			"isDeleted": false,
			"id": "RT0iWn0hXhSYb49iOzYI5",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 899.1851032576528,
			"y": 1534.7737004682917,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 73.78503795322627,
			"height": 62.90729606904847,
			"seed": 485112534,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1707208495319,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "jjc6fJ0OfMgPy2Z4CXlUy",
				"gap": 1.2368421052633494,
				"focus": 0.5964645047292387
			},
			"endBinding": {
				"elementId": "vx5PT4yf",
				"gap": 13.55674342105192,
				"focus": -1.472585739094363
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					73.78503795322627,
					-62.90729606904847
				]
			]
		},
		{
			"type": "rectangle",
			"version": 388,
			"versionNonce": 202774058,
			"isDeleted": false,
			"id": "jcfNzIZfQ-P2D-SIUOAY-",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 113.81668220502104,
			"y": 1696.5672153192118,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 322,
			"height": 59,
			"seed": 540847830,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "9t8P9BGS"
				}
			],
			"updated": 1699273156023,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 227,
			"versionNonce": 2023569782,
			"isDeleted": false,
			"id": "9t8P9BGS",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 219.32840095502104,
			"y": 1714.0672153192118,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 110.9765625,
			"height": 24,
			"seed": 699163670,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "vector batch",
			"rawText": "vector batch",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "jcfNzIZfQ-P2D-SIUOAY-",
			"originalText": "vector batch",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "rectangle",
			"version": 534,
			"versionNonce": 1443217642,
			"isDeleted": false,
			"id": "CFiTe8YnaROUs4LizF41U",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 60.07984009975792,
			"y": 1564.988267950791,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 425.1578947368421,
			"height": 210.5789473684208,
			"seed": 1447480266,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 148,
			"versionNonce": 1863552693,
			"isDeleted": false,
			"id": "NRlF12hV",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 84.2903664155474,
			"y": 1574.488267950791,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 38.984375,
			"height": 24,
			"seed": 438230026,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699323680498,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "Task",
			"rawText": "Task",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Task",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "text",
			"version": 147,
			"versionNonce": 1756996379,
			"isDeleted": false,
			"id": "vx5PT4yf",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 923.2377348366,
			"y": 1434.4882679507914,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 47.5390625,
			"height": 24,
			"seed": 1340114954,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "pjtODo5pl-owDTxml6xKf",
					"type": "arrow"
				},
				{
					"id": "RT0iWn0hXhSYb49iOzYI5",
					"type": "arrow"
				}
			],
			"updated": 1699323680499,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "merge",
			"rawText": "merge",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "merge",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "text",
			"version": 174,
			"versionNonce": 1400500245,
			"isDeleted": false,
			"id": "usiFav72",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 275.8693137839689,
			"y": 1514.4882679507919,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 86.2890625,
			"height": 24,
			"seed": 1762944150,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699323680499,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "partition",
			"rawText": "partition",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "partition",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "rectangle",
			"version": 349,
			"versionNonce": 905398,
			"isDeleted": false,
			"id": "YisGBxNhiQGLjb8JbFLtg",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -106.57031469900369,
			"y": 1104.4032635221415,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 1414,
			"height": 720,
			"seed": 77394710,
			"groupIds": [
				"v3hEGVKvc3u0sqOwU76wD"
			],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "PYE_0NkjbmzhEQ-LXpfHy",
					"type": "arrow"
				},
				{
					"id": "HcNhqWClRqF_WH6r7HGpa",
					"type": "arrow"
				}
			],
			"updated": 1699273192196,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 283,
			"versionNonce": 255321398,
			"isDeleted": false,
			"id": "RW60pcrQ",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 394.3171381976888,
			"y": 1045.49113610529,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 360,
			"height": 48,
			"seed": 1008074518,
			"groupIds": [
				"v3hEGVKvc3u0sqOwU76wD"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "OmniRuntime native shuffle\n占用大量内存，但无需持有多个文件句柄",
			"rawText": "OmniRuntime native shuffle\n占用大量内存，但无需持有多个文件句柄",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "OmniRuntime native shuffle\n占用大量内存，但无需持有多个文件句柄",
			"lineHeight": 1.2,
			"baseline": 43
		},
		{
			"type": "text",
			"version": 48,
			"versionNonce": 762087355,
			"isDeleted": false,
			"id": "3dskBaTI",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1216.7721155120794,
			"y": -289.582722281105,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 260.9765625,
			"height": 24,
			"seed": 1251292036,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699323680501,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "map*reduce*executor个小文件",
			"rawText": "map*reduce*executor个小文件",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "map*reduce*executor个小文件",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "text",
			"version": 82,
			"versionNonce": 323822965,
			"isDeleted": false,
			"id": "ZGSHiltx",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1203.9031941648286,
			"y": 58.873891785281785,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 210.0390625,
			"height": 24,
			"seed": 430894212,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699323680502,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "reducer*executor个文件",
			"rawText": "reducer*executor个文件",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "reducer*executor个文件",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "image",
			"version": 447,
			"versionNonce": 1659960298,
			"isDeleted": false,
			"id": "Yen04XoJ44Tck3K_NhQc3",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -846.404316915718,
			"y": 1015.7067009802081,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 711.8797747810595,
			"height": 457.97598844248165,
			"seed": 1113655882,
			"groupIds": [
				"CzNaiulupcWCGfsgHXPE2"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "yLA_Bww1lYOWEG7R_T17A",
					"type": "arrow"
				},
				{
					"id": "s8Ijd5vfARR8PHVta8CY5",
					"type": "arrow"
				}
			],
			"updated": 1699273156023,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "4f9553304cce93389e2065b89f5963a9296ecaac",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "text",
			"version": 67,
			"versionNonce": 1872353371,
			"isDeleted": false,
			"id": "JZPAgToH",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -576.3309804031635,
			"y": 1017.7408702655637,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 207.265625,
			"height": 24,
			"seed": 1982370180,
			"groupIds": [
				"CzNaiulupcWCGfsgHXPE2"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699323680502,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "BypassMergeSortShuffle",
			"rawText": "BypassMergeSortShuffle",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "BypassMergeSortShuffle",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "text",
			"version": 253,
			"versionNonce": 1372761813,
			"isDeleted": false,
			"id": "MprMud7S",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -936.8038773027976,
			"y": 1374.521782158714,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 211.8359375,
			"height": 24,
			"seed": 639395716,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699323680503,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "executor*Reducer个文件",
			"rawText": "executor*Reducer个文件",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "executor*Reducer个文件",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "image",
			"version": 446,
			"versionNonce": 1444751606,
			"isDeleted": false,
			"id": "HJLQ2rrhKtNMOE3a41pzl",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -896.0714940129193,
			"y": 356.0050737549945,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 728.5318466010438,
			"height": 603.7679829629445,
			"seed": 2138997130,
			"groupIds": [
				"lgcD3dD_RNcMabhN8G7HP",
				"BVlfaFiK51UCQYTIJ-7lx"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "tdhpmyk1w6ZHjFgI5tb-L",
					"type": "arrow"
				}
			],
			"updated": 1699273156024,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "12d401376e1e0b86ed2a98b77185be95a309d658",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "text",
			"version": 434,
			"versionNonce": 1830032635,
			"isDeleted": false,
			"id": "dhw2DzKA",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -602.8071138120213,
			"y": 378.78631753027526,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 133.7122344970703,
			"height": 31.391179439582658,
			"seed": 2119112470,
			"groupIds": [
				"lgcD3dD_RNcMabhN8G7HP",
				"BVlfaFiK51UCQYTIJ-7lx"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699323680503,
			"link": null,
			"locked": false,
			"fontSize": 26.159316199652217,
			"fontFamily": 4,
			"text": "sortShuffle",
			"rawText": "sortShuffle",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "sortShuffle",
			"lineHeight": 1.2,
			"baseline": 24
		},
		{
			"type": "text",
			"version": 217,
			"versionNonce": 765463605,
			"isDeleted": false,
			"id": "9eNW8JbL",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -910.259235829769,
			"y": 849.317090156644,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 211.8359375,
			"height": 24,
			"seed": 1718794044,
			"groupIds": [
				"BVlfaFiK51UCQYTIJ-7lx"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699323680504,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "executor*Reducer个文件",
			"rawText": "executor*Reducer个文件",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "executor*Reducer个文件",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "rectangle",
			"version": 87,
			"versionNonce": 1801309226,
			"isDeleted": false,
			"id": "XsufvaWcr1IpvXCjA43Kb",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -842.6557585320502,
			"y": 575.0141714118328,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 315.69162894709274,
			"height": 84.37403896784178,
			"seed": 1886024964,
			"groupIds": [
				"BVlfaFiK51UCQYTIJ-7lx"
			],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "dQNJ3rkcmTTAKGhACn0ZV",
					"type": "arrow"
				}
			],
			"updated": 1699273156024,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 169,
			"versionNonce": 1067047526,
			"isDeleted": false,
			"id": "dQNJ3rkcmTTAKGhACn0ZV",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -523.1720379459534,
			"y": 597.3477956356147,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 394.3775304564281,
			"height": 28.207074256772216,
			"seed": 209977788,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1706323522204,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "XsufvaWcr1IpvXCjA43Kb",
				"focus": -0.5856573705179259,
				"gap": 3.7920916390039565
			},
			"endBinding": {
				"elementId": "zATQgjeO",
				"focus": 0.26960269202898945,
				"gap": 8.218863828761187
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					394.3775304564281,
					28.207074256772216
				]
			]
		},
		{
			"type": "text",
			"version": 166,
			"versionNonce": 90029467,
			"isDeleted": false,
			"id": "de9w8rht",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 437.59877236976683,
			"y": 1932.4569660772636,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 755.791259765625,
			"height": 57.56181246836163,
			"seed": 24306,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "PYE_0NkjbmzhEQ-LXpfHy",
					"type": "arrow"
				}
			],
			"updated": 1699323680505,
			"link": "[[Spark Native列式Shuffle.pptx]]",
			"locked": false,
			"fontSize": 47.968177056968024,
			"fontFamily": 4,
			"text": "📍[[Spark Native列式Shuffle.pptx]]",
			"rawText": "[[Spark Native列式Shuffle.pptx]]",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "📍[[Spark Native列式Shuffle.pptx]]",
			"lineHeight": 1.2,
			"baseline": 45
		},
		{
			"type": "arrow",
			"version": 186,
			"versionNonce": 1175755190,
			"isDeleted": false,
			"id": "PYE_0NkjbmzhEQ-LXpfHy",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 862.9580152534143,
			"y": 1834.4910569863546,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 51.36181190775119,
			"height": 92.00000000000045,
			"seed": 2030557546,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1699273399206,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "YisGBxNhiQGLjb8JbFLtg",
				"focus": -0.06193557929278837,
				"gap": 10.087793464213064
			},
			"endBinding": {
				"elementId": "de9w8rht",
				"focus": 0.31243258981640926,
				"gap": 5.9659090909085535
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					51.36181190775119,
					92.00000000000045
				]
			]
		},
		{
			"type": "embeddable",
			"version": 183,
			"versionNonce": 749111281,
			"isDeleted": false,
			"id": "V_k65EI6JDJ0dU-0s3kNF",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1148.1951278234442,
			"y": 2397.9998289161786,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 560,
			"height": 840,
			"seed": 1246483306,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "Dt-OLJhVo9-wX5PQSFl8x",
					"type": "arrow"
				}
			],
			"updated": 1707208495177,
			"link": "https://blog.csdn.net/lidongmeng0213/article/details/109409210",
			"locked": false,
			"validated": true,
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 71,
			"versionNonce": 821951990,
			"isDeleted": false,
			"id": "s8Ijd5vfARR8PHVta8CY5",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -640.2336796016978,
			"y": 1486.4208815477587,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 106.94369872091943,
			"height": 75.78947368420995,
			"seed": 1498515626,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1699273156024,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Yen04XoJ44Tck3K_NhQc3",
				"focus": -0.2771470927994242,
				"gap": 12.738192125068736
			},
			"endBinding": {
				"elementId": "ntB1icr2lXcIimKL9kVwa",
				"focus": -0.34084142816785173,
				"gap": 11.578947368420813
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-106.94369872091943,
					75.78947368420995
				]
			]
		},
		{
			"type": "arrow",
			"version": 139,
			"versionNonce": 24519418,
			"isDeleted": false,
			"id": "Dt-OLJhVo9-wX5PQSFl8x",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -780.5763136783156,
			"y": 2275.8945657582844,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 44.20083137773031,
			"height": 108.42105263157919,
			"seed": 2054285622,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1703483695259,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "ntB1icr2lXcIimKL9kVwa",
				"focus": -0.40405659570830144,
				"gap": 7.368421052631675
			},
			"endBinding": {
				"elementId": "V_k65EI6JDJ0dU-0s3kNF",
				"focus": -0.2956074396517614,
				"gap": 13.684210526314928
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-44.20083137773031,
					108.42105263157919
				]
			]
		},
		{
			"type": "image",
			"version": 76,
			"versionNonce": 1934522166,
			"isDeleted": false,
			"id": "ntB1icr2lXcIimKL9kVwa",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1433.67989236638,
			"y": 1573.7893026003896,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1053.0747922437674,
			"height": 694.7368421052632,
			"seed": 1390986090,
			"groupIds": [
				"TBEC9G6SkKYLZ5e2lFogE"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "s8Ijd5vfARR8PHVta8CY5",
					"type": "arrow"
				},
				{
					"id": "Dt-OLJhVo9-wX5PQSFl8x",
					"type": "arrow"
				},
				{
					"id": "EiuvY9OY5ogIeuKBU7PK5",
					"type": "arrow"
				}
			],
			"updated": 1699273169443,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "45645fedb59c90cd58a4b5e1a5ec32ce17cc6336",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "text",
			"version": 108,
			"versionNonce": 1452981653,
			"isDeleted": false,
			"id": "vU3AdB1g",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -574.3819082510763,
			"y": 1665.3682499688105,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 252.3828125,
			"height": 24,
			"seed": 556983722,
			"groupIds": [
				"TBEC9G6SkKYLZ5e2lFogE"
			],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1699323680506,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "spark.shuffle.file.buffer=32k",
			"rawText": "spark.shuffle.file.buffer=32k",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "spark.shuffle.file.buffer=32k",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "text",
			"version": 301,
			"versionNonce": 2112162879,
			"isDeleted": false,
			"id": "engw6p6o",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -332.96409369515595,
			"y": 1873.5086008460044,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 771.7578125,
			"height": 192,
			"seed": 1731370218,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "EiuvY9OY5ogIeuKBU7PK5",
					"type": "arrow"
				},
				{
					"id": "HcNhqWClRqF_WH6r7HGpa",
					"type": "arrow"
				}
			],
			"updated": 1707208521186,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "当前Omni shuffle的实现与bypass几乎一样，除了spark.shuffle.file.buffer设置为了2GB，\n因而减少了生成的文件\n问题：\n1. 没有一直持有文件句柄，因而一个分区可能会生成多个小文件，\n而bypass一直持有，一个分区对应一个文件\n2.当前的buffer内存未被统计，executor offheap memory中，\n当一个节点运行多个task时，可能存在大量未被统计的内存使用，\n如典配下：96核*2GB=192GB内存未被统计，导致杀进程",
			"rawText": "当前Omni shuffle的实现与bypass几乎一样，除了spark.shuffle.file.buffer设置为了2GB，\n因而减少了生成的文件\n问题：\n1. 没有一直持有文件句柄，因而一个分区可能会生成多个小文件，\n而bypass一直持有，一个分区对应一个文件\n2.当前的buffer内存未被统计，executor offheap memory中，\n当一个节点运行多个task时，可能存在大量未被统计的内存使用，\n如典配下：96核*2GB=192GB内存未被统计，导致杀进程",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "当前Omni shuffle的实现与bypass几乎一样，除了spark.shuffle.file.buffer设置为了2GB，\n因而减少了生成的文件\n问题：\n1. 没有一直持有文件句柄，因而一个分区可能会生成多个小文件，\n而bypass一直持有，一个分区对应一个文件\n2.当前的buffer内存未被统计，executor offheap memory中，\n当一个节点运行多个task时，可能存在大量未被统计的内存使用，\n如典配下：96核*2GB=192GB内存未被统计，导致杀进程",
			"lineHeight": 1.2,
			"baseline": 187
		},
		{
			"type": "arrow",
			"version": 354,
			"versionNonce": 961562751,
			"isDeleted": false,
			"id": "EiuvY9OY5ogIeuKBU7PK5",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -360.8267067708141,
			"y": 1845.2199498117945,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 23.5874905515916,
			"height": 21.033483577283278,
			"seed": 277276650,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1707208521186,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "ntB1icr2lXcIimKL9kVwa",
				"focus": -0.7083928288116734,
				"gap": 19.778393351798513
			},
			"endBinding": {
				"elementId": "engw6p6o",
				"focus": -0.5559090827131711,
				"gap": 8.421052631579187
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					23.5874905515916,
					21.033483577283278
				]
			]
		},
		{
			"type": "arrow",
			"version": 358,
			"versionNonce": 600405183,
			"isDeleted": false,
			"id": "HcNhqWClRqF_WH6r7HGpa",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -122.93196992870867,
			"y": 1811.327316384574,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 20.652936316097595,
			"height": 56.918126566693445,
			"seed": 1811965354,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1707208521186,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "YisGBxNhiQGLjb8JbFLtg",
				"focus": 0.6089177569784873,
				"gap": 16.361655229705093
			},
			"endBinding": {
				"elementId": "engw6p6o",
				"focus": -0.5544004896361544,
				"gap": 5.263157894737105
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-20.652936316097595,
					56.918126566693445
				]
			]
		},
		{
			"type": "text",
			"version": 114,
			"versionNonce": 1066714682,
			"isDeleted": false,
			"id": "CauKfj2d",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -416.39889916366565,
			"y": 2504.5589723674025,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 213.34152221679688,
			"height": 76.79906268306969,
			"seed": 786929958,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1703483698048,
			"link": null,
			"locked": false,
			"fontSize": 21.33307296751936,
			"fontFamily": 4,
			"text": "1630 没有12大盘场景；\n7270 920b 64核\n",
			"rawText": "1630 没有12大盘场景；\n7270 920b 64核\n",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "1630 没有12大盘场景；\n7270 920b 64核\n",
			"lineHeight": 1.2,
			"baseline": 71
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#e03131",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 1,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 4,
		"currentItemFontSize": 20,
		"currentItemTextAlign": "center",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 1917.046034580333,
		"scrollY": 120.92019429926562,
		"zoom": {
			"value": 0.7499999999999998
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"gridColor": {
			"Bold": "#C9C9C9FF",
			"Regular": "#EDEDEDFF"
		},
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		}
	},
	"files": {}
}
```
%%
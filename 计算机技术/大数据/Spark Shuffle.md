---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
BypassMergeSortShuffleWriter
与优化后的hashshuffle区别在于
hashshuffle合并同一分区的mapper task到一个文件，便于reducer拉取
Bypass合并reducer 所需文件到一个文件，提供index（从原来的一个
task输出n个文件，缩减为一个task输出1个文件+index）
 ^sbquvKrx

1.这里其实只有一个内存buffer，这里多个buffer是指多个sort批次
2.why when reducer become bigger prefer using sortshuffle
sortshuffle只需开一个buffer，而bypass需要为每个分区开一个buffer,
因而一方面占用内存（32KB each partition），更重要的是持有太多文件句柄
3. 多个磁盘文件进行归并排序，并通过索引文件确定分区 ^zATQgjeO

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

executor*mapper个文件 ^MprMud7S

[[Spark Native列式Shuffle.pptx]] ^de9w8rht

当前Omni shuffle的实现与bypass几乎一样，除了spark.shuffle.file.buffer设置为了2GB，
因而减少了生成的文件
问题：
1. 没有一直持有文件句柄，因而一个分区可能会生成多个小文件，
而bypass一直持有，一个分区对应一个文件
2.当前的buffer内存未被统计（更新：已统计），executor offheap memory中，
当一个节点运行多个task时，可能存在大量未被统计的内存使用，
如典配下：96核*2GB=192GB内存未被统计，导致杀进程 ^engw6p6o

示意 ^PgImpot8


# Embedded files
748dbc03407c93be6466bdf211b21aee5e8ea9c2: [[绘图/attachments/20240206163724.jpg]]
d1640c5484326b1f7bcff95a385b7bfafb03550b: [[绘图/attachments/20240206195032.jpg]]
0313131d6cd2c2dc8a5531d91a01f23b4ff58dc1: [[绘图/attachments/20240206202543.jpg]]
940597a0f51e21c8b50d341a23fadec021bb5c56: [[绘图/attachments/Pasted Image 20240206202757_074.jpg]]
e4eb39e08814d5189208887ec133cbc78383c8cf: [[绘图/attachments/Pasted Image 20240206202923_955.jpg]]
820d7ae40979e9f69acd01696ec673fb2140bfe5: [[绘图/attachments/20240206202955.jpg]]

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.0.20",
	"elements": [
		{
			"type": "image",
			"version": 123,
			"versionNonce": 1186433942,
			"isDeleted": false,
			"id": "qGOA0orT",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -852.1668068159453,
			"y": 1023.5206555358327,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 680.0573729732026,
			"height": 428.896509432971,
			"seed": 95404,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "s8Ijd5vfARR8PHVta8CY5",
					"type": "arrow"
				},
				{
					"id": "yLA_Bww1lYOWEG7R_T17A",
					"type": "arrow"
				}
			],
			"updated": 1709260190990,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "0313131d6cd2c2dc8a5531d91a01f23b4ff58dc1",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "image",
			"version": 214,
			"versionNonce": 1258889418,
			"isDeleted": false,
			"id": "q0UfM9A5",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -912.8402730400112,
			"y": 322.9317252298215,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 733.2136357987532,
			"height": 635.5811322664678,
			"seed": 7843,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "tdhpmyk1w6ZHjFgI5tb-L",
					"type": "arrow"
				}
			],
			"updated": 1709260190990,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "d1640c5484326b1f7bcff95a385b7bfafb03550b",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 152,
			"versionNonce": 506308822,
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
			"updated": 1709260190990,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 277,
			"versionNonce": 1669232522,
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
			"updated": 1709260190990,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 966,
			"versionNonce": 1754792266,
			"isDeleted": false,
			"id": "sbquvKrx",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1656.836312911549,
			"y": 1167.0476021965474,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 772.3818359375,
			"height": 182.11592111733154,
			"seed": 1975430422,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1712473596733,
			"link": null,
			"locked": false,
			"fontSize": 25.293877932962715,
			"fontFamily": 4,
			"text": "BypassMergeSortShuffleWriter\n与优化后的hashshuffle区别在于\nhashshuffle合并同一分区的mapper task到一个文件，便于reducer拉取\nBypass合并reducer 所需文件到一个文件，提供index（从原来的一个\ntask输出n个文件，缩减为一个task输出1个文件+index）\n",
			"rawText": "BypassMergeSortShuffleWriter\n与优化后的hashshuffle区别在于\nhashshuffle合并同一分区的mapper task到一个文件，便于reducer拉取\nBypass合并reducer 所需文件到一个文件，提供index（从原来的一个\ntask输出n个文件，缩减为一个task输出1个文件+index）\n",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "BypassMergeSortShuffleWriter\n与优化后的hashshuffle区别在于\nhashshuffle合并同一分区的mapper task到一个文件，便于reducer拉取\nBypass合并reducer 所需文件到一个文件，提供index（从原来的一个\ntask输出n个文件，缩减为一个task输出1个文件+index）\n",
			"lineHeight": 1.2,
			"baseline": 176
		},
		{
			"type": "text",
			"version": 362,
			"versionNonce": 1486550602,
			"isDeleted": false,
			"id": "zATQgjeO",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -120.57564366076417,
			"y": 619.8406564516418,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 857.45849609375,
			"height": 151.57894736842096,
			"seed": 1020426710,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "dQNJ3rkcmTTAKGhACn0ZV",
					"type": "arrow"
				},
				{
					"id": "k_gvwaHCVNIQC_zmgs15-",
					"type": "arrow"
				}
			],
			"updated": 1709260190990,
			"link": null,
			"locked": false,
			"fontSize": 25.26315789473683,
			"fontFamily": 4,
			"text": "1.这里其实只有一个内存buffer，这里多个buffer是指多个sort批次\n2.why when reducer become bigger prefer using sortshuffle\nsortshuffle只需开一个buffer，而bypass需要为每个分区开一个buffer,\n因而一方面占用内存（32KB each partition），更重要的是持有太多文件句柄\n3. 多个磁盘文件进行归并排序，并通过索引文件确定分区",
			"rawText": "1.这里其实只有一个内存buffer，这里多个buffer是指多个sort批次\n2.why when reducer become bigger prefer using sortshuffle\nsortshuffle只需开一个buffer，而bypass需要为每个分区开一个buffer,\n因而一方面占用内存（32KB each partition），更重要的是持有太多文件句柄\n3. 多个磁盘文件进行归并排序，并通过索引文件确定分区",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "1.这里其实只有一个内存buffer，这里多个buffer是指多个sort批次\n2.why when reducer become bigger prefer using sortshuffle\nsortshuffle只需开一个buffer，而bypass需要为每个分区开一个buffer,\n因而一方面占用内存（32KB each partition），更重要的是持有太多文件句柄\n3. 多个磁盘文件进行归并排序，并通过索引文件确定分区",
			"lineHeight": 1.2,
			"baseline": 145
		},
		{
			"type": "embeddable",
			"version": 100,
			"versionNonce": 1265494870,
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
			"updated": 1709260190990,
			"link": "https://medium.com/@philipp.brunenberg/understanding-apache-spark-hash-shuffle-b9aed2d587b0",
			"locked": false,
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 82,
			"versionNonce": 1530502410,
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
			"updated": 1709260190990,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 290,
			"versionNonce": 1149374614,
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
			"updated": 1709260190990,
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
			"version": 1313,
			"versionNonce": 755194018,
			"isDeleted": false,
			"id": "tdhpmyk1w6ZHjFgI5tb-L",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -933.6227620139621,
			"y": 584.4314160621832,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 149.7396967457762,
			"height": 37.44794835780283,
			"seed": 1118011990,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1715841715465,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "BxKSYaDIcXvzqPTatvR6G",
				"gap": 11.024211702168714,
				"focus": 0.6171395888169293
			},
			"endBinding": {
				"elementId": "RRuSFIIYJTjtc4J48l8Yp",
				"gap": 3.567640186468225,
				"focus": -0.4559683917720346
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
					-149.7396967457762,
					37.44794835780283
				]
			]
		},
		{
			"type": "arrow",
			"version": 1403,
			"versionNonce": 1914378274,
			"isDeleted": false,
			"id": "yLA_Bww1lYOWEG7R_T17A",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -876.77129316635,
			"y": 1131.7921958236166,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 208.70114801549448,
			"height": 420.4202529613251,
			"seed": 25950422,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1715841715466,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "qGOA0orT",
				"gap": 24.60448635040467,
				"focus": -0.6986286770992105
			},
			"endBinding": {
				"elementId": "RRuSFIIYJTjtc4J48l8Yp",
				"gap": 1.4576577643620112,
				"focus": -0.5678566255496715
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
					-208.70114801549448,
					-420.4202529613251
				]
			]
		},
		{
			"type": "rectangle",
			"version": 162,
			"versionNonce": 394879626,
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
			"updated": 1709260190991,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 192,
			"versionNonce": 169566998,
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
			"updated": 1709260190991,
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
			"version": 218,
			"versionNonce": 1108377930,
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
			"updated": 1709260190991,
			"link": null,
			"locked": false
		},
		{
			"type": "line",
			"version": 100,
			"versionNonce": 103452758,
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
			"updated": 1709260190991,
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
			"version": 118,
			"versionNonce": 868599818,
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
			"updated": 1709260190991,
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
			"version": 110,
			"versionNonce": 711071126,
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
			"updated": 1709260190991,
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
			"version": 189,
			"versionNonce": 73377982,
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
			"updated": 1716173680592,
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
			"baseline": 33
		},
		{
			"type": "text",
			"version": 210,
			"versionNonce": 2146890454,
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
			"updated": 1709260190991,
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
			"version": 493,
			"versionNonce": 1827207074,
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
			"updated": 1715841715470,
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
			"version": 281,
			"versionNonce": 561915926,
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
			"updated": 1709260190991,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 194,
			"versionNonce": 1525189706,
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
			"updated": 1709260190991,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 212,
			"versionNonce": 250393942,
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
			"updated": 1709260190991,
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
			"version": 432,
			"versionNonce": 696719010,
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
			"updated": 1715841715474,
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
			"version": 340,
			"versionNonce": 828033570,
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
			"updated": 1716173680594,
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
			"baseline": 66
		},
		{
			"type": "text",
			"version": 181,
			"versionNonce": 1042800894,
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
			"updated": 1716173680595,
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
			"baseline": 18
		},
		{
			"type": "text",
			"version": 275,
			"versionNonce": 25245154,
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
			"updated": 1716173680597,
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
			"baseline": 31
		},
		{
			"type": "rectangle",
			"version": 328,
			"versionNonce": 1870051466,
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
			"updated": 1709260190991,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 167,
			"versionNonce": 1926655254,
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
			"updated": 1709260190991,
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
			"version": 719,
			"versionNonce": 43890082,
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
			"updated": 1715841715477,
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
			"version": 639,
			"versionNonce": 1619146018,
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
			"updated": 1715841715478,
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
			"version": 431,
			"versionNonce": 1691721226,
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
			"updated": 1709260190991,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 254,
			"versionNonce": 862101398,
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
			"updated": 1709260190991,
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
			"version": 850,
			"versionNonce": 938267810,
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
			"updated": 1715841715480,
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
			"version": 552,
			"versionNonce": 1817590998,
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
			"updated": 1709260190991,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 374,
			"versionNonce": 1490625418,
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
			"updated": 1709260190991,
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
			"version": 572,
			"versionNonce": 392442390,
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
			"updated": 1709260190991,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 399,
			"versionNonce": 633348682,
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
			"updated": 1709260190991,
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
			"version": 576,
			"versionNonce": 903189538,
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
			"updated": 1715841715480,
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
			"version": 780,
			"versionNonce": 691303330,
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
			"updated": 1715841715482,
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
			"version": 390,
			"versionNonce": 151200918,
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
			"updated": 1709260190991,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 229,
			"versionNonce": 1470076874,
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
			"updated": 1709260190991,
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
			"version": 536,
			"versionNonce": 631120342,
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
			"updated": 1709260190991,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 157,
			"versionNonce": 985600318,
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
			"updated": 1716173680598,
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
			"baseline": 18
		},
		{
			"type": "text",
			"version": 156,
			"versionNonce": 560212386,
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
			"updated": 1716173680598,
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
			"baseline": 18
		},
		{
			"type": "text",
			"version": 183,
			"versionNonce": 897988990,
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
			"updated": 1716173680599,
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
			"baseline": 18
		},
		{
			"type": "rectangle",
			"version": 351,
			"versionNonce": 164897878,
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
			"updated": 1709260190991,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 292,
			"versionNonce": 2016585058,
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
			"updated": 1716173680600,
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
			"baseline": 42
		},
		{
			"type": "text",
			"version": 57,
			"versionNonce": 1438538174,
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
			"updated": 1716173680600,
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
			"baseline": 18
		},
		{
			"type": "text",
			"version": 91,
			"versionNonce": 792439074,
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
			"updated": 1716173680601,
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
			"baseline": 18
		},
		{
			"type": "text",
			"version": 268,
			"versionNonce": 847802878,
			"isDeleted": false,
			"id": "MprMud7S",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -932.0577835527976,
			"y": 1374.521782158714,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 202.34375,
			"height": 24,
			"seed": 639395716,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1716173680601,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "executor*mapper个文件",
			"rawText": "executor*mapper个文件",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "executor*mapper个文件",
			"lineHeight": 1.2,
			"baseline": 18
		},
		{
			"type": "arrow",
			"version": 402,
			"versionNonce": 70613386,
			"isDeleted": false,
			"id": "dQNJ3rkcmTTAKGhACn0ZV",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -530.7562212239618,
			"y": 591.5482884294956,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 401.96171373443644,
			"height": 37.42169785858937,
			"seed": 209977788,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1709260190991,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "BxKSYaDIcXvzqPTatvR6G",
				"focus": -0.3588128241859227,
				"gap": 13.581188097170525
			},
			"endBinding": {
				"elementId": "zATQgjeO",
				"focus": 0.22455127818816426,
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
					401.96171373443644,
					37.42169785858937
				]
			]
		},
		{
			"type": "text",
			"version": 175,
			"versionNonce": 1844327650,
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
			"updated": 1716173680603,
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
			"baseline": 46
		},
		{
			"type": "arrow",
			"version": 188,
			"versionNonce": 253868106,
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
			"updated": 1709260190991,
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
			"version": 297,
			"versionNonce": 925649238,
			"isDeleted": false,
			"id": "V_k65EI6JDJ0dU-0s3kNF",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1508.4438335288355,
			"y": 2378.091347811406,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 1426.4929395124411,
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
			"updated": 1709260190991,
			"link": "https://blog.csdn.net/lidongmeng0213/article/details/109409210",
			"locked": false,
			"scale": [
				1,
				1
			]
		},
		{
			"type": "arrow",
			"version": 399,
			"versionNonce": 331335626,
			"isDeleted": false,
			"id": "s8Ijd5vfARR8PHVta8CY5",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -661.2392403478053,
			"y": 1478.8366982697503,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 138.02686311163518,
			"height": 90.0098173304757,
			"seed": 1498515626,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "PgImpot8"
				}
			],
			"updated": 1712473706398,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "qGOA0orT",
				"focus": -0.32920123774097626,
				"gap": 26.41953330094634
			},
			"endBinding": {
				"elementId": "yq9bTB0vZ_jaDps2pz1xE",
				"focus": -0.3812607595649242,
				"gap": 12.781585604691031
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
					-138.02686311163518,
					90.0098173304757
				]
			]
		},
		{
			"type": "text",
			"version": 2,
			"versionNonce": 1799321866,
			"isDeleted": false,
			"id": "PgImpot8",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -750.252671903623,
			"y": 1511.8416069349882,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 40,
			"height": 24,
			"seed": 1970867414,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1712473705580,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "示意",
			"rawText": "示意",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "s8Ijd5vfARR8PHVta8CY5",
			"originalText": "示意",
			"lineHeight": 1.2,
			"baseline": 19
		},
		{
			"type": "arrow",
			"version": 605,
			"versionNonce": 616869526,
			"isDeleted": false,
			"id": "Dt-OLJhVo9-wX5PQSFl8x",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -901.1711396195313,
			"y": 2224.7013286317288,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.924423370318777,
			"height": 139.7058086533625,
			"seed": 2054285622,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1709260190991,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "yq9bTB0vZ_jaDps2pz1xE",
				"focus": -0.015284603892089663,
				"gap": 17.378106991132086
			},
			"endBinding": {
				"elementId": "V_k65EI6JDJ0dU-0s3kNF",
				"focus": -0.07613553203509112,
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
					11.924423370318777,
					139.7058086533625
				]
			]
		},
		{
			"type": "text",
			"version": 320,
			"versionNonce": 1457881662,
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
			"updated": 1716173680607,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 4,
			"text": "当前Omni shuffle的实现与bypass几乎一样，除了spark.shuffle.file.buffer设置为了2GB，\n因而减少了生成的文件\n问题：\n1. 没有一直持有文件句柄，因而一个分区可能会生成多个小文件，\n而bypass一直持有，一个分区对应一个文件\n2.当前的buffer内存未被统计（更新：已统计），executor offheap memory中，\n当一个节点运行多个task时，可能存在大量未被统计的内存使用，\n如典配下：96核*2GB=192GB内存未被统计，导致杀进程",
			"rawText": "当前Omni shuffle的实现与bypass几乎一样，除了spark.shuffle.file.buffer设置为了2GB，\n因而减少了生成的文件\n问题：\n1. 没有一直持有文件句柄，因而一个分区可能会生成多个小文件，\n而bypass一直持有，一个分区对应一个文件\n2.当前的buffer内存未被统计（更新：已统计），executor offheap memory中，\n当一个节点运行多个task时，可能存在大量未被统计的内存使用，\n如典配下：96核*2GB=192GB内存未被统计，导致杀进程",
			"textAlign": "center",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "当前Omni shuffle的实现与bypass几乎一样，除了spark.shuffle.file.buffer设置为了2GB，\n因而减少了生成的文件\n问题：\n1. 没有一直持有文件句柄，因而一个分区可能会生成多个小文件，\n而bypass一直持有，一个分区对应一个文件\n2.当前的buffer内存未被统计（更新：已统计），executor offheap memory中，\n当一个节点运行多个task时，可能存在大量未被统计的内存使用，\n如典配下：96核*2GB=192GB内存未被统计，导致杀进程",
			"lineHeight": 1.2,
			"baseline": 186
		},
		{
			"type": "arrow",
			"version": 645,
			"versionNonce": 18300581,
			"isDeleted": false,
			"id": "EiuvY9OY5ogIeuKBU7PK5",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -451.83690610691343,
			"y": 1837.4884455306205,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 110.45175978017829,
			"height": 50.800321366806884,
			"seed": 277276650,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1715223330128,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "yq9bTB0vZ_jaDps2pz1xE",
				"focus": -0.5277809368579394,
				"gap": 12.36281766735732
			},
			"endBinding": {
				"elementId": "engw6p6o",
				"focus": -0.36614047774058267,
				"gap": 8.421052631579244
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
					110.45175978017829,
					50.800321366806884
				]
			]
		},
		{
			"type": "arrow",
			"version": 386,
			"versionNonce": 624531813,
			"isDeleted": false,
			"id": "HcNhqWClRqF_WH6r7HGpa",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -120.18458059526995,
			"y": 1833.478258065473,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 17.143483905665278,
			"height": 34.76718488579445,
			"seed": 1811965354,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1715223330129,
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
					-17.143483905665278,
					34.76718488579445
				]
			]
		},
		{
			"type": "rectangle",
			"version": 63,
			"versionNonce": 349077782,
			"isDeleted": false,
			"id": "sMecAvQ0Z24r3yxVssl9_",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -521.5848594871077,
			"y": 673.4221536634305,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 344.13231623962383,
			"height": 140.30739064315244,
			"seed": 861760447,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "k_gvwaHCVNIQC_zmgs15-",
					"type": "arrow"
				}
			],
			"updated": 1709260190991,
			"link": null,
			"locked": false
		},
		{
			"type": "arrow",
			"version": 72,
			"versionNonce": 1176912714,
			"isDeleted": false,
			"id": "k_gvwaHCVNIQC_zmgs15-",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -176.45254324748385,
			"y": 749.1893343439338,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 41.66103093879627,
			"height": 17.809992477908054,
			"seed": 462025663,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1709260190991,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "sMecAvQ0Z24r3yxVssl9_",
				"focus": 0.553879310344829,
				"gap": 1
			},
			"endBinding": {
				"elementId": "zATQgjeO",
				"focus": 0.592923352380903,
				"gap": 14.215868647923344
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
					41.66103093879627,
					-17.809992477908054
				]
			]
		},
		{
			"type": "image",
			"version": 11,
			"versionNonce": 1221193302,
			"isDeleted": false,
			"id": "i5kBrlwS",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -909.0481814010071,
			"y": -889.5895763417458,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 500,
			"height": 275.40983606557376,
			"seed": 3528,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709260190991,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "748dbc03407c93be6466bdf211b21aee5e8ea9c2",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "rectangle",
			"version": 44,
			"versionNonce": 1943226890,
			"isDeleted": false,
			"id": "BxKSYaDIcXvzqPTatvR6G",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -922.5985503117934,
			"y": 540.6989462982866,
			"strokeColor": "#e03131",
			"backgroundColor": "transparent",
			"width": 378.26114099066103,
			"height": 119.45088662862975,
			"seed": 230147697,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "dQNJ3rkcmTTAKGhACn0ZV",
					"type": "arrow"
				},
				{
					"id": "tdhpmyk1w6ZHjFgI5tb-L",
					"type": "arrow"
				}
			],
			"updated": 1709260190991,
			"link": null,
			"locked": false
		},
		{
			"type": "image",
			"version": 64,
			"versionNonce": 1566946198,
			"isDeleted": false,
			"id": "yq9bTB0vZ_jaDps2pz1xE",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -1407.5420183223455,
			"y": 1581.628101204917,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 943.3422945480748,
			"height": 625.6951204356797,
			"seed": 1396991,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "s8Ijd5vfARR8PHVta8CY5",
					"type": "arrow"
				},
				{
					"id": "EiuvY9OY5ogIeuKBU7PK5",
					"type": "arrow"
				},
				{
					"id": "Dt-OLJhVo9-wX5PQSFl8x",
					"type": "arrow"
				}
			],
			"updated": 1709260190991,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "940597a0f51e21c8b50d341a23fadec021bb5c56",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "image",
			"version": 57,
			"versionNonce": 1538357450,
			"isDeleted": false,
			"id": "vHSezlvtD2HmRk_OMRjaQ",
			"fillStyle": "solid",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -930.9788779245362,
			"y": -119.19262410681844,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 758.4293578315331,
			"height": 419.60440803105536,
			"seed": 867140497,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709260190991,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "e4eb39e08814d5189208887ec133cbc78383c8cf",
			"scale": [
				1,
				1
			]
		},
		{
			"type": "image",
			"version": 101,
			"versionNonce": 215404758,
			"isDeleted": false,
			"id": "xk1ElFM6",
			"fillStyle": "hachure",
			"strokeWidth": 1,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -923.0348484760852,
			"y": -556.7375508267858,
			"strokeColor": "transparent",
			"backgroundColor": "transparent",
			"width": 667.1120164158465,
			"height": 359.3668897954411,
			"seed": 52199,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1709260190991,
			"link": null,
			"locked": false,
			"status": "pending",
			"fileId": "820d7ae40979e9f69acd01696ec673fb2140bfe5",
			"scale": [
				1,
				1
			]
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
		"scrollX": 1584.0393838451778,
		"scrollY": -974.4278397302602,
		"zoom": {
			"value": 0.8348939081797636
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
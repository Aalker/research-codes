---
title: "Functional Enrichment for Anvio"
author: "Amanda Alker"
date: "3/8/2019"
output: 
  html_document: 
    keep_md: yes
---



Load dplyr, a data manipulation package

```r
library("dplyr")
```

```
## Warning: package 'dplyr' was built under R version 3.5.2
```

```
## 
## Attaching package: 'dplyr'
```

```
## The following objects are masked from 'package:stats':
## 
##     filter, lag
```

```
## The following objects are masked from 'package:base':
## 
##     intersect, setdiff, setequal, union
```

```r
library("openxlsx")
```

##Functional anlysis output table by clade for Pangenomic analysis

Read the functional file in as a table


```r
Functional_file = read.table("Pluteo-Pan-enriched-functions-clade", header = TRUE, sep = "\t")
```

Create an subset table that identifies enrichment by corrected p-value and selects the entire row


```r
significant_genes_all = filter(Functional_file, Functional_file$corrected_p_value <= 0.05 )
View(significant_genes_all)
```

Reduce the table by getting rid of negative enrichment scores. Negative enrichment scores are when the occurrence of a function in the group is lower than outside the group. This just means that the hit for significance is redundant across groups.


```r
significant_genes = filter(significant_genes_all, significant_genes_all$enrichment_score > 0)
View(significant_genes)
```

Core genes in group


```r
core_genes_in_group = filter(significant_genes, significant_genes$core_in_group == "True") 
View(core_genes_in_group)
```

Not core genes in group


```r
not_core_genes_in_group = filter(significant_genes, significant_genes$core_in_group == "False") 
View(not_core_genes_in_group)
```

Export to Excel files

```r
write.xlsx (core_genes_in_group, "Anvio_pangenome_core_genes")
write.xlsx(not_core_genes_in_group, "Anvio_pangenome_not_core_genes")
```


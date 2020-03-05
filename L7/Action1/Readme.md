1、将csv格式的rating数据转化成libfm格式：  
'perl triple_format_to_libfm.pl -in ./movielens/ratings.csv -target 2   -separator ","'  
2、使用libfm进行训练，输出结果文件 Action1_movielens_out：  
'libFM -task r -train ./movielens/ratings.csv.libfm -test ./movielens/ratings.csv.libfm -dim '1,1,8' -method sgd -learn_rate 0.01 -out Action1_movielens_out.txt'

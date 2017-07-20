# -*- coding: utf-8 -*-
import pandas
import sqlite3
import json        
import sys

# UnicodeEncodeError: 'ascii' codec can't //通过以下语句修改编码设置解决
reload(sys)
sys.setdefaultencoding( "utf-8" )

tmp_mp3 = [
"http://bos.nj.bpc.baidu.com/v1/developer/39cb48e4-bd09-4e9d-933c-be8bfea0cb45.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/ff390320-372f-4564-87ad-e7eb5cf3f90b.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/ad3240d0-9b50-491f-98a5-d0b956a9f426.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/c303922d-194c-4015-9377-fbf811010a3d.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/eaab7248-af7a-4cd1-94b2-27ddb12ea65a.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/8f5ad243-d684-4443-a3bc-16e6924ae0a4.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/00a81304-25d8-4f31-88b4-44a9b7e620d2.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/24f0aea6-1757-4fec-98b7-30cb483e70c2.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/b3675dd1-5378-43ca-90cc-467c433aab3b.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/f4e9efb0-9207-4f81-93bf-d3871fc33c2a.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/17c99ecd-4ee0-442e-989c-bf26a1c0eca0.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/8855ebb1-0b5f-47a9-96bd-4fd2c9559b83.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/676ded6f-d94a-417e-b5cc-b8ec3aebcff4.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/d5bbfae3-2b1b-4b5a-a2ee-702e64214809.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/207adf7b-99c3-4a0b-a6ac-b89b1d783858.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/97fea474-2512-407b-9c9f-9fadf7306216.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/638792d8-4544-46cf-92cc-88a32ea153cf.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/d648c408-7f89-4185-aa61-77d31080d60a.mp3",
"http://bos.nj.bpc.baidu.com/v1/developer/e4700f90-0b96-40d0-8a9d-5b53bc0626b3.mp3"
]
divs_story = ""
divs_link = ""    
with sqlite3.connect('..\qzstorys.sqlite') as db:
    df = pandas.read_sql_query('SELECT * FROM qzstory',con = db)
    for i in range(0,len(df)):
        divs_story += """
            <div class="col-xs-6 col-lg-4">
              <h2>%s</h2>
              <p><audio controls><source src="%s" type="audio/mpeg">您的浏览器不支持 audio 元素。</audio></p>              
              <p>%s</p>
              <p><a class="btn btn-default" href="%s" role="button">听故事 &raquo;</a></p>
            </div><!--/.col-xs-6.col-lg-4-->
        """ % (df['story_title'][i],tmp_mp3[i],df['story_content'][i],tmp_mp3[i])
        divs_link += """
            <a href="%s" class="list-group-item">%s</a>
        """ % (df['story_url'][i],df['story_title'][i])    
    
    
with open('stories.html',"w") as file:
    str =  """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="../favicon.ico">

    <title>QzStory</title>

    <!-- Bootstrap core CSS -->
    <link href="../dist/css/bootstrap.min.css" rel="stylesheet">

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="../assets/css/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="starter-template.css" rel="stylesheet">
    <link href="offcanvas.css" rel="stylesheet">
    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="../../assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="../assets/js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <nav class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">QzStory</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="active"><a href="#">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container">

      <div class="row row-offcanvas row-offcanvas-right">

        <div class="col-xs-12 col-sm-9">
          <p class="pull-right visible-xs">
            <button type="button" class="btn btn-primary btn-xs" data-toggle="offcanvas">故事列表</button>
          </p>
          <div class="jumbotron">
            <h2>QzStory</h2>
            <p>陪伴孩子，促进孩子与家长共同成长和进步</p>
          </div>
          <div class="row">
            %s
          </div><!--/row-->
        </div><!--/.col-xs-12.col-sm-9-->

        <div class="col-xs-6 col-sm-3 sidebar-offcanvas" id="sidebar">
          <div class="list-group">
            %s
          </div>
        </div><!--/.sidebar-offcanvas-->
      </div><!--/row-->

      <hr>

      <footer>
        <p>&copy; 2017 WYP.</p>
      </footer>

    </div><!--/.container-->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="../dist/js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="../assets/js/ie10-viewport-bug-workaround.js"></script>
    <script src="offcanvas.js"></script>    
  </body>
</html>
    """ % (divs_story,divs_link)
    file.write(str)



import urllib

def get_page(url):
    try:
        a = urllib.urlopen(url).read()
        print a
        return a
    except:
        return ""

    
def get_next_target(page):
    start_link = page.find('window.location.href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find("'", start_link)
    end_quote = page.find("'", start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)
        
def add_to_index(index, keyword, url):
    if keyword in index:
        index[keyword].append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None
    
def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index, graph

index, graph = crawl_web('http://bitfountain.io/course/the-complete-ios-7-course-learn-by-building-14-apps')


if __name__ == '__main__':

    page = """


<!DOCTYPE html>
<html lang="en" style="height:100%;">
  <head>
    <!-- Meta, title, CSS, favicons, etc. -->
    <meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="">
<meta name="author" content="">

<link rel="icon" 
      type="image/png" 
      href="https://s3.amazonaws.com/lecture_attachments/ISryEFNGQguq17uQaVt7_whale.png">
<link rel="stylesheet" href="http://bitfountain.io/css/redactor.css" />
<link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet">
<title>
  
bitfountain - Get Started Now</title>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
	<script src="http://bitfountain.io/js/jquery.placeholder.js"></script>


				<script src="https://a59b98a46b6b6225f8e5-f63a39482042e1d18f69fa58fccf96e8.ssl.cf5.rackcdn.com/bootstrap.js"></script>
		<script src="http://bitfountain.io/js/bootstrap-switch.js"></script>
	<script src="https://ankur.usefedora.com/flat/js/flatui-radio.js"></script>

	<link href="https://a59b98a46b6b6225f8e5-f63a39482042e1d18f69fa58fccf96e8.ssl.cf5.rackcdn.com/bootstrap.css" rel="stylesheet">
	<link href="http://bitfountain.io/css/switch2.css" rel="stylesheet">
	<link href="http://bitfountain.io/css/docs.css" rel="stylesheet">
		<link href="http://bitfountain.io/css/school.css" rel="stylesheet">
	<link href="http://bitfountain.io/css/datepicker.css" rel="stylesheet">
	
				<link href="https://a59b98a46b6b6225f8e5-f63a39482042e1d18f69fa58fccf96e8.ssl.cf5.rackcdn.com/flat-ui.css" rel="stylesheet">

				
  </head>
  <body style="overflow-x:hidden;">
	<style>
		.navbar-brand
	{
		background-image:url('https://s3.amazonaws.com/lecture_attachments/u40Vtk5GTG23D2Y3GHq0_whale.png');
		background-size: 100% 100%;
		height:60px;
		width:68px;
	}
			#homepage_div
	{
		background-image:url("https://ankur.usefedora.com/images/background_phone.png");
		background-position:50% 50%;
		background-size:cover;
		height:90%;
	}
	.page_div
	{
		background-image:url("https://s3.amazonaws.com/lecture_attachments/msax2HBCSSqtiS75M1nb_sos.png");
		background-size:auto;
	}
	.bs-docs-nav .navbar-nav > li > a {
	  color: #eeeeee;
	}
	.bs-docs-nav .navbar-nav > li > a:hover {
	  color: #ffffff;
	}
	
	.dropdown-menu > .active > a, .dropdown-menu > .active > a:hover, .dropdown-menu > .active     >     a:focus {
	    background-color: #34495e !important;
	    background-image: linear-gradient(to bottom, #17AA76, #149466) !important;
	    background-repeat: repeat-x !important;
	    color: #FFFFFF;
	    outline: 0 none;
	    text-decoration: none;
	}
	
	.dropdown.open {
	    background: #34495e;
	}
		</style>
    <!-- Page content of course! -->
    <!-- Custom styles for this template -->
<style>
  body {
    padding-top: 0px;
	height:100%;
  }
 

.navbar-el
{
	height:60px;
}
.navbar-active
{
	height:60px;
	background-color:#34495e;
	color:#ffffff;
}
.navbar-el:hover
{
	background-color:#34495e;
		color:#ffffff;
}
.navbar-link
{
	height:60px;
	padding-top:21px;
	font-size:18px;
}
.nopadh2
{
padding-top:0px; margin-top:0px;padding-bottom:0px;margin-bottom:0px;	
}

</style>





	<style type="text/css">
	
		@media screen and (max-width: 900px){
			#course_sidebar
			{
				display:none;
				width:100%;
				background-color:#ecf0f1;
				border-right:1px solid #bdc3c7;
			}
			#main_content
			{
				padding-left:25px;
				padding-right:25px;
				padding-top:70px;
			}
			#menu_button {
				display:inline-block;
			}
			.course_headline
			{
				font-size:28px;
			}
			.imptd
			{
				font-size:15px;
			}
		}
			@media screen and (min-width: 900px){

			#course_sidebar
			{
				width:275px; margin-top:40px;background-color:#ecf0f1;height:100%;padding-left:0px;padding-right:0px;border-right:1px solid #bdc3c7;position:fixed;overflow:scroll;
			}
			
			#main_content
			{
				margin-left:275px;padding:40px;padding-top:70px;
			}
			#menu_button {
				display:none;
			}
		}
	.menu_maindiv
	{
		padding-left:25px;
		font-size:17px;
		padding-top:8px;
		padding-bottom:8px;

		cursor: pointer;
	}
	.menu_maindiv_active
	{
			color:#ffffff;
			background-color:#34495e;

	}

	#secondarynav
	{
		background-color:#2c3e50;
		height:40px;
		border-bottom:1px solid #34495e;
		top:0;
		position:fixed;
		width:100%;
		z-index:100;
	}
	.icon_div
	{
		display:inline-block;
	}
	
	.menu_maindiv:hover
	{
		color:#ffffff;
		background-color:#34495e;
	}
	.new_menuitem
	{
		margin-left:10px;
	}
		.menu_maindiv_active a
		{
				color:#ffffff !important;
		}
	.menu_maindiv:hover a
	{
	color:#ffffff;
	}
	.menu_maindiv a
	{
		color:#34495e;

	}
	.nav-el2
	{
		cursor:pointer;
	}
	.nav-el2:hover
	{
			background-color: #34495e !important;
	}
	
	.nav_icon
	{
		width:40px;
		font-size:24px;
		padding:6px;
		padding-left:15px;
		padding-right:15px;
			box-shadow:0px 0px 2px #888;
			cursor:pointer;
				  color: #eeeeee;

	}
	.nav_icon:hover
	{
		color:#ffffff;
		background-color:#34495e;
	}
	
	</style>
	
	<div id="secondarynav">

	<div class="icon_div"><a class="nav_icon" href="http://bitfountain.io/you"><i style="padding-top:5px;" class="fa fa-chevron-circle-left"></i></a></div>
<div class="icon_div" id="menu_button" onClick="toggleMenu()"><a class="nav_icon"><i style="padding-top:5px;" class="fa fa-list"></i></a></div>

<div class="icon_div pull-right"><a class="nav_icon" href="mailto:john@bitfountain.io" target="_blank"><i style="padding-top:5px;" class="fa fa-question-circle"></i></a></div>
	</div>
	<div style="" id="course_sidebar">
	
		<div style="padding-top:10px;padding-bottom:10px;padding:0px;background-color:#2C3E50;font-size:17px;color:#eee;"><img src="https://s3.amazonaws.com/lecture_attachments/1935.jpg" id="main_course_image" style="width:100%;"/></div>
	<div style="padding-left:15px;padding-right:15px;font-size:20px;font-weight:bold;text-align:center;margin-top:8px;">The Complete iOS 7 Course - Learn by Building 14 Apps<hr style="background-color:#7f8c8d;color:#7f8c8d,border-color:#7f8c8d;margin-bottom:0px;" /></div>
<div style="margin-bottom:25px;margin-top:-5px;padding-left:15px;padding-right:15px;">	<div class="progress progress-striped" style="height:25px;border:1px solid #ccc;">
	  <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%; height:25px;"><div style="width:200px;padding-left:6px;padding-top:6px;font-size:16px;text-shadow:0px 0px 5px #111;">0% COMPLETE</div>
	    <span class="sr-only"></span>
	  </div>
	</div>
	</div>
	
			<div id="button_0" class="menu_maindiv menu_maindiv_active"><i style="font-size:20px;" class="fa fa-list-alt"></i><a href="#" class="new_menuitem"  onClick="navigate(0)">
				Class Curriculum
			  </a></div>
			
			
			<div id="button_1" class="menu_maindiv  "><i style="font-size:20px;" class="fa fa-user"></i><a href="#" class="new_menuitem"  onClick="navigate(1)">
				Your Instructor
			  </a></div>
			
			
			<div id="button_2" onClick="navigate(2)" class="menu_maindiv  "><i style="font-size:20px;" class="fa fa-edit"></i><a href="#" class="new_menuitem"  onClick="navigate(2)">
				Write a Review
			  </a></div>
	
	</div>
	<div style="" id="main_content">
	


<style type="text/css">

.section
{
	font-size:20px;
	font-weight:bold;
	padding:10px;
	padding-top:18px;
}
.lecture
{

	font-size:18px;
	padding:10px;
	padding-top:4px;
	padding-bottom:4px;
	padding-left:0px;
	cursor:pointer;

}
.nav-tabs .active a
{
	font-weight:bold;
}
.container {
  margin: 0px auto;
  padding: 0px;
}

#main { 
  background: #3B3B3B;
  height: 430px;
}
.redeem_field
{
	margin-top:7px;
}
.content {
  padding: 10px 44px;
}

.text {
  border-bottom: 1px solid #262626;
  margin-top: 40px;
  padding-bottom: 40px;
  text-align: center;
}

.text h2 {
  color: #E5E5E5;
  font-size: 20px;
  font-style: normal;
  font-variant: normal;
  font-weight: lighter;
  letter-spacing: 2px;
}

.counter {
  background: #2C2C2C;
  -moz-box-shadow:    inset 0 0 5px #000000;
  -webkit-box-shadow: inset 0 0 5px #000000;
  box-shadow:         inset 0 0 5px #000000;
  min-height: 100px;
  text-align: center;
}

.counter h3 {
  color: #E5E5E5;
  font-size: 12px;
  font-style: normal;
  font-variant: normal;
  font-weight: lighter;
  letter-spacing: 1px;
  padding-top: 20px;
  margin-bottom: 30px;
}

#countdown {
  color: #FFFFFF;
}

#countdown span {
  color: #E5E5E5;
	color:white;
  font-size: 22px;
  font-weight: bold;
  margin-left: 0px;
  margin-right: 0px;
  text-align: center;
	text-shadow: 0px 0px 1px #000;
}
.lecture_tr
{
	cursor: pointer !important;
}
.lecture_tr:hover
{
	color:#ffffff !important;
	background-color:#34495e !important;
	
}
.lecture_tr:hover i{
	color:#ffffff !important;
}

.table-hover>tbody>tr:hover>td, .table-hover>tbody>tr:hover>th {
 	color:#ffffff !important;
	background-color:#34495e !important;
}

span.hidden-xs {display:inline !important;}

@media (max-width: 768px) { 
span.hidden-xs {display:none !important;}
}
</style>

<div class="row">

	<div class="container">

			<div class="col-lg-12">
		
<h3 style="margin-top:0px;" class="course_headline"><i class="fa fa-list-alt"></i> Course Curriculum</h3>	<hr />				
	
	<div class="well well-sm" style="padding-left:20px;padding-right:20px;">
		<div class="row"><div class="col-lg-9 col-md-9 col-sm-9 col-xs-8" style="padding-left:10px;padding-top:4px;font-size:18px;">Next Lecture: <span class="hidden-xs"><b>Opening XCode</b></span></div>
			<div class="col-lg-3 col-md-3 col-sm-3 col-xs-4"><a class="btn btn-sm btn-primary btn-block" href="http://bitfountain.io/lecture/44412/opening-xcode/">Start</a></div>
			</div>
	</div>
	
	
												

						<div class="section">Section 1 - Your First App!</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44411/introduction';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																		<i class="fa fa-check-circle" id="circle_44411"></i>
									</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Introduction   (00:22)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44412/opening-xcode';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44412"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Opening XCode   (06:07)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44413/label-use';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44413"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Label Use   (07:04)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44414/buttons';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44414"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Buttons   (09:54)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44415/colors';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44415"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Colors   (04:58)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44416/uitextfield';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44416"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">UITextField   (06:12)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44417/uinavigationcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44417"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">UINavigationController  &nbsp;<i class='fa fa-paperclip'></i>  (07:00)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 2 - Resources</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44419/resources';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44419"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Resources  &nbsp;<i class='fa fa-paperclip'></i> </span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 3 - Variables</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44421/what-is-a-variable';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44421"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">What is A Variable?   (06:43)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44422/intro-to-commenting';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44422"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Intro to Commenting   (03:05)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44423/operations-on-variables';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44423"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Operations on Variables   (05:44)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44424/logging-into-the-console';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44424"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Logging into the Console   (03:51)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44425/valid-variable-names';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44425"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Valid Variable Names   (04:11)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44426/tokens';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44426"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Tokens   (05:14)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44427/converting-units-part-1';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44427"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Converting Units Part 1   (06:39)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44428/converting-units-part-2';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44428"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Converting Units Part 2   (06:21)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 4 - Challenge 1: Age of Laika</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44430/age-of-laika';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44430"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Age of Laika  &nbsp;<i class='fa fa-paperclip'></i> </span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44431/age-of-laika-part-1';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44431"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Age of Laika Part 1   (05:14)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44432/age-of-laika-part-2';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44432"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Age of Laika Part 2   (03:34)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 5 - If Statements</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44434/if-statements';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44434"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">If Statements   (05:32)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44435/bools';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44435"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">BOOLS   (03:03)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44436/if-statements-contd';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44436"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">If Statements Cont'd   (04:33)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 6 - Challenge 2: For Loops</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44438/age-of-laika-control-flow';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44438"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Age of Laika Control Flow   (05:29)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44439/for-loops';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44439"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">For Loops   (04:00)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44440/for-loops-part-2';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44440"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">For Loops Part 2   (04:47)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 7 - Challenge 3: 99 Sodas</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44442/99-sodas';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44442"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">99 Sodas   (02:53)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 8 - Intro to Object Oriented Programming</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44444/create-a-new-project';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44444"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Create A New Project   (02:07)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44445/what-are-classes-and-objects';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44445"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">What are Classes and Objects   (03:15)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44446/make-your-own-class';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44446"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Make Your Own Class   (03:12)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44447/header-file';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44447"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Header File   (04:43)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44448/implementation-file';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44448"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementation File   (02:43)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 9 - Properties</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44450/properties';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44450"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Properties   (07:47)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44451/instantiating-an-object';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44451"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Instantiating an Object   (01:05)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44452/import';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44452"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Import   (03:56)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44453/instantiating-an-object-contd';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44453"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Instantiating an Object Cont'd   (03:59)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44454/setting-properties';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44454"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting Properties   (09:56)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 10 - Methods</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44456/methods';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44456"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Methods   (03:03)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44457/implementing-our-methods';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44457"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing our Methods   (04:41)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44458/methods-with-arguements';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44458"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Methods with Arguements   (06:13)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44459/self-properties';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44459"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Self Properties   (05:48)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44460/self-methods';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44460"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Self Methods   (05:33)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44461/methods-with-multiple-arguments';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44461"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Methods with Multiple Arguments   (06:11)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44462/methods-with-return-values';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44462"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Methods with Return Values   (06:05)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44463/review-weekly-recap';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44463"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Review (weekly recap)   (07:06)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 11 - Challenge 4: Methods</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44465/the-challenge';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44465"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">The Challenge  </span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44466/methods-solution';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44466"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Methods Solution   (08:26)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 12 - Classes</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44468/add-some-flare-ui-elements';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44468"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">ADD SOME FLARE (UI ELEMENTS)   (11:35)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44469/multiple-dogs';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44469"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Multiple Dogs  &nbsp;<i class='fa fa-paperclip'></i>  (10:47)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44470/nsmutablearray';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44470"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSMutableArray   (02:07)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44471/documentation';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44471"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Documentation   (02:25)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44472/multiple-dogs-continued';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44472"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Multiple Dogs Continued   (09:22)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 13 - Extra Credit: Animations</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44474/ec-animation-strictly-for-extra-credit';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44474"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">EC: Animation (strictly for Extra Credit)   (05:36)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 14 - Challenge 5: Debug Recurring Dog</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44476/the-challenge';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44476"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">The Challenge  </span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44477/recuring-dog-pictures';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44477"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Recuring Dog Pictures   (03:13)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 15 - Inheritance</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44479/inheritance';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44479"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Inheritance   (02:30)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44480/subclassing-mbfdog';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44480"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Subclassing MBFDog   (07:39)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44481/implementing-a-superclass-method';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44481"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing a Superclass Method   (02:17)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44482/super';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44482"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Super   (01:27)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 16 - Object Continued</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44484/the-difference-between-objects-and-primitives';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44484"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">The Difference Between Objects and Primitives   (03:43)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44485/nsstring';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44485"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSString   (04:14)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44486/iterating-through-an-array';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44486"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Iterating through an Array   (07:43)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44487/whats-really-going-on-properties';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44487"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">What's Really Going On Properties   (07:00)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 17 - Pirate Adventure Assignment: Prereq's</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44489/nsarray-initializer-and-embedded-array';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44489"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSArray Initializer and Embedded Array   (05:38)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44490/cgpoint';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44490"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">CGPoint   (02:20)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44491/embedded-if-statements';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44491"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Embedded If Statements   (02:46)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44492/buttons-and-alertviews';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44492"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Buttons and AlertViews   (05:30)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44493/property-of-a-custom-class';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44493"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Property of a Custom Class   (02:46)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44494/introduction-to-nil-video';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44494"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Introduction to nil (video)   (02:33)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 18 - Pirate Adventure Assignment</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44496/pirate-assignment';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44496"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Pirate Assignment  &nbsp;<i class='fa fa-paperclip'></i> </span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44497/pirate-game-introduction';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44497"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Pirate Game Introduction  &nbsp;<i class='fa fa-paperclip'></i>  (13:17)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 19 - Pirate Adventure Solutions: Parts 1 & 2</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44499/pirate-storyboard-setup';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44499"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Pirate Storyboard Setup   (15:46)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44500/hooking-up-the-view';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44500"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Hooking up the View   (05:04)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44501/creating-our-tile-object';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44501"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Creating our tile object   (03:26)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44502/factory-object';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44502"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Factory Object   (10:20)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44503/factory-explained';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44503"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Factory Explained   (04:04)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44504/setting-up-the-initial-tile';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44504"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting up the Initial Tile   (08:05)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44505/hiding-our-buttons-dynamically';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44505"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Hiding our Buttons Dynamically   (11:49)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44506/navigating-between-tiles';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44506"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Navigating Between Tiles   (04:59)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44507/add-a-story-and-images';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44507"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Add a Story and Images   (13:12)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 20 - A Review</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44509/review-week2-wrap';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44509"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Review (week2 wrap)   (09:48)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44510/you-did-it';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44510"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">You did it!  </span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 21 - Pirate Adventure Solutions: Part 3</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44512/weapon-and-armor-class';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44512"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Weapon and Armor Class   (02:17)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44513/creating-a-character-class';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44513"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Creating a Character Class   (03:24)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44514/create-a-character';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44514"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Create a Character   (05:56)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44515/adding-a-character-to-the-application';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44515"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a Character to the Application   (04:50)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 22 - Pirate Adventure Solutions: Part 4</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44517/updating-the-tile-model';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44517"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Updating the Tile Model   (11:00)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44518/implementing-our-action-changes';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44518"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing our Action Changes   (06:03)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44519/finishing-our-action-changes';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44519"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Finishing our Action Changes   (03:23)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44520/create-a-boss';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44520"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Create a Boss   (02:30)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44521/implementing-our-boss';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44521"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing our Boss   (02:09)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44522/alerting-the-user';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44522"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Alerting the User   (04:01)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44523/clean-up-and-a-reset-button';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44523"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Clean up and a Reset Button   (03:20)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 23 - Pirate Adventure Wrap Up</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44525/pirate-assignment-solution';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44525"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Pirate Assignment Solution  </span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 24 - Terminal and Git</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44527/terminal';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44527"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Terminal   (06:10)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44528/git-part-1';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44528"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Git Part 1   (09:53)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44529/git-part-2';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44529"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Git Part 2   (04:13)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 25 - Introduction to MVC</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44531/mvc-overview';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44531"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">MVC Overview   (03:48)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44532/communication-between-the-view-controller-and-modelviews';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44532"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Communication between the View Controller and Model/Views   (03:09)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44533/communication-from-the-view-and-model-to-the-view-controller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44533"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Communication from the View and Model to the View Controller   (06:06)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 26 - Introduction to UITableView</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44535/practice-using-uitableview';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44535"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Practice Using UITableView   (03:38)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44536/new-project';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44536"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">New Project   (08:39)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44537/a-quick-look-at-our-data-source';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44537"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">A Quick Look at our Data Source   (05:31)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44538/nsindexpath';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44538"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NsIndexPath   (02:44)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44539/nsindexpath-contd';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44539"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSIndexPath Cont'd   (03:30)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44540/having-our-tableview-display-our-model';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44540"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Having our TableView display our Model   (06:33)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44541/model';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44541"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Model   (02:44)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 27 - Third Party Library</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44543/nsdictionary';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44543"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSDictionary  &nbsp;<i class='fa fa-paperclip'></i>  (05:45)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44544/utilizing-our-new-model';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44544"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Utilizing our new Model  &nbsp;<i class='fa fa-paperclip'></i>  (04:30)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44545/nsnumber';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44545"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSNumber   (03:12)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44546/define';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44546"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">#define   (02:03)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44547/literals-review';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44547"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Literals Review   (03:39)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44548/class-methods';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44548"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Class Methods   (02:30)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 28 - Review</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44550/section-3-review';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44550"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Section 3 Review   (11:22)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 29 - Challenge 6: UITableViewController</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44552/the-challenge';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44552"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">The Challenge  </span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44553/uitableviewcontroller-solution';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44553"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">UITableViewController Solution   (12:09)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 30 - Models and Space Object</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44555/making-a-spaceobject-class';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44555"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Making a SpaceObject Class  &nbsp;<i class='fa fa-paperclip'></i>  (02:06)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44556/literals-contd';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44556"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Literals Cont'd   (01:15)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44557/custom-initializers';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44557"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Custom Initializers   (15:46)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44558/lets-create-and-use-space-objects';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44558"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Lets Create and Use Space Objects  &nbsp;<i class='fa fa-paperclip'></i>  (10:14)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 31 - Challenge 7: User Data Model</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44560/the-challenge-user-data-model';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44560"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">The Challenge: User Data Model  &nbsp;<i class='fa fa-paperclip'></i> </span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44561/solution-part-1';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44561"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Solution Part 1   (13:38)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44562/solution-part-2';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44562"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Solution Part 2   (05:41)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 32 - Transitioning to a Second View Controller</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44564/uinavigationcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44564"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">UINavigationController   (04:30)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44565/push-segue';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44565"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Push Segue   (02:23)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44566/setting-up-our-second-view-controller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44566"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting up our Second View Controller   (04:34)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 33 - UIScrollView</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44568/uiscrollview-a-closer-look';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44568"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">UIScrollView - A Closer Look   (02:28)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44569/setting-up-our-uiscrollview';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44569"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting up our UIScrollView   (03:22)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44570/zooming';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44570"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Zooming   (03:50)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44571/setting-our-viewcontroller-as-a-delegate';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44571"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting our ViewController as a Delegate   (07:35)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 34 - Challenge 8: UIScrollView</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44573/the-challenge';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44573"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">The Challenge  &nbsp;<i class='fa fa-paperclip'></i> </span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44574/uiscrollview-solution';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44574"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">UIScrollView Solution   (07:42)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 35 - Passing Data between View Controllers</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44576/passing-data-forward';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44576"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Passing Data Forward   (03:02)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44577/id-and-introspection';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44577"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">id and introspection   (02:08)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44578/implementing-introspection-and-passing-the-data';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44578"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing Introspection and Passing the Data   (10:48)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44579/passing-information-to-proxy-properties-instead-of-outlets';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44579"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Passing information to Proxy Properties instead of Outlets   (04:47)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 36 - Challenge 9: Passing Data</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44581/the-challenge';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44581"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">The Challenge  </span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44582/passing-information-to-another-viewcontroller-solution';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44582"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Passing Information to another ViewController Solution   (09:23)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 37 - Displaying our SpaceData</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44584/adding-another-uitableview-part-1';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44584"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding another UITableView Part 1   (05:34)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44585/adding-another-uitable-part-2';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44585"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding Another UITable Part 2   (10:08)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44586/writing-the-logic-behind-our-space-data-table-view-controller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44586"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Writing the Logic behind our Space Data Table View Controller   (10:21)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44587/adding-a-method-from-our-uitableviewdelegate';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44587"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a Method from our UITableViewDelegate   (04:48)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44588/performing-the-segue';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44588"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Performing the Segue   (07:43)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 38 - Challenge 10: UITableView</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44590/the-challenge';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44590"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">The Challenge  </span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44591/uitableview-solution';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44591"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">UITableView Solution   (08:56)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 39 - Review</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44593/review';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44593"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Review   (07:55)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 40 - Introduction to Protocols and Delegation</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44595/chance-of-us-discovering-a-new-planet';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44595"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Chance of us Discovering a New Planet   (06:55)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44596/designing-our-new-view-controller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44596"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Designing our New View Controller   (12:16)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44597/one-more-segue';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44597"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">One more Segue!   (03:56)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44598/protocols-in-objective-c';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44598"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Protocols in Objective-C   (11:28)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 41 - Implementing our Own Protocls</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44600/our-own-protocol-part-1';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44600"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Our Own Protocol Part 1   (05:50)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44601/our-own-protocol-part-2';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44601"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Our Own Protocol Part 2   (04:01)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44602/our-own-protocol-part-3';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44602"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Our Own Protocol Part 3   (02:52)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44603/our-own-protocol-part-4';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44603"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Our Own Protocol Part 4   (03:25)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44604/our-own-protocol-part-5';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44604"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Our Own Protocol Part 5   (04:07)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 42 - Finishing Touches on Protcols</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44606/reload-data';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44606"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Reload Data   (04:18)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44607/loose-ends';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44607"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Loose Ends   (03:17)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44608/solution-no-more-mercury';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44608"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Solution - No More Mercury   (05:12)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44609/lazy-instantiation';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44609"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Lazy Instantiation   (06:44)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 43 - Challenge 11: Protocols and Delegation</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44611/the-challenge';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44611"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">The Challenge  </span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44612/protocols-and-delegation-solution';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44612"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Protocols and Delegation Solution   (06:45)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44613/protocols-and-delegation-extra-credit';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44613"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Protocols and Delegation Extra Credit   (04:43)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 44 - Intro to Persistence</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44615/persistence-overview';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44615"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Persistence Overview   (02:15)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44616/nsuserdefaults';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44616"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSUserDefaults   (03:45)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 45 - Data Persistence NSUserDefaults</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44618/getting-our-space-objects-into-tip-top-property-list-shape';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44618"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Getting our Space Objects into Tip Top Property List Shape   (06:32)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44619/back-to-our-nsuserdefaults';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44619"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Back to our NSUserDefaults   (07:51)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44620/retrieving-our-data';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44620"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Retrieving our Data   (06:00)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44621/deleting-some-cells-from-out-uitableview';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44621"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Deleting some Cells from out UITableView   (08:05)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 46 - Challenge 12: NSUserDefaults, Segues and Protocols</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44623/the-challenge';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44623"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">The Challenge  </span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44624/nsuser-defaults-segues-and-protocols-solution-part-1';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44624"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSUser Defaults, Segues and Protocols Solution Part 1   (13:45)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44625/nsuser-defaults-segues-and-protocols-solution-part-2';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44625"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSUser Defaults, Segues and Protocols Solution Part 2   (03:57)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44626/nsuser-defaults-segues-and-protocols-solution-part-3';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44626"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSUser Defaults, Segues and Protocols Solution Part 3   (07:54)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44627/nsuser-defaults-segues-and-protocols-solution-part-4';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44627"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSUser Defaults, Segues and Protocols Solution Part 4   (06:37)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44628/nsuser-defaults-segues-and-protocols-solution-part-5';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44628"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSUser Defaults, Segues and Protocols Solution Part 5   (05:34)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44629/nsuser-defaults-segues-and-protocols-solution-part-6';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44629"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSUser Defaults, Segues and Protocols Solution Part 6   (02:45)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 47 - Review</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44631/review';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44631"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Review   (06:56)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 48 - Overdue Task List Assignment: Prereq's</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44633/pch-file';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44633"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">.PCH File   (03:01)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44634/textview-and-the-keyboard';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44634"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">TextView and the Keyboard   (05:17)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44635/nsdate-datepicker-nsdataformatter-and-timeinterval';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44635"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSDate, Datepicker, NSDataFormatter and TimeInterval   (06:31)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44636/insert-and-remove-objects-from-a-nsmutablearray';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44636"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Insert and Remove Objects from a NSMutableArray   (03:40)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 49 - Overdue Task List Assignment</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44638/overdue-task-list-assignment';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44638"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Overdue Task List Assignment  </span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 50 - Overdue Task List Assignment:  Part 1</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44640/setting-up-the-storyboard-part-1';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44640"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting up the Storyboard Part 1   (05:52)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44641/setting-up-the-storyboard-part-2';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44641"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting up the Storyboard Part 2   (06:03)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44642/iboutlets';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44642"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">IBOutlets   (06:43)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 51 - Overdue Task List Assignment:  Part 2</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44644/setup-our-defines';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44644"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setup our #defines   (02:25)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44645/creating-a-task-model';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44645"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Creating a Task Model   (03:49)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44646/implement-the-custom-initializers';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44646"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implement the Custom Initializers   (04:01)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 52 - Overdue Task List Assignment:  Part 3</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44648/protocol-for-the-cancel-and-add-task-buttons';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44648"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Protocol for the Cancel and Add Task Buttons   (03:42)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44649/call-the-delegate-methods-in-the-cancel-and-addtask-actions';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44649"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Call the Delegate Methods in the Cancel and AddTask Actions   (03:08)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44652/an-array-to-hold-the-tasks';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44652"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">An Array to hold the Tasks   (03:10)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44653/implementing-the-delegate-methods-and-saving-the-task';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44653"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing the Delegate Methods and Saving the Task   (10:29)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44654/segue-to-the-addtaskviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44654"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Segue to the AddTaskViewController   (04:53)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 53 - Overdue Task List Assignment:  Part 4</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44656/access-nsuserdefaults-to-setup-the-taskobjects-array';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44656"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Access NSUserDefaults to Setup the taskObjects Array   (04:00)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 54 - Overdue Task List Assignment:  Part 5</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44658/setup-the-viewcontrollers-tableviewdatasource';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44658"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setup the ViewController's TableViewDataSource   (09:42)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 55 - Overdue Task List Assignment:  Part 6</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44660/color-coding-the-uitableviewcells';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44660"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Color Coding the UiTableViewCells   (05:31)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44661/completing-a-task';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44661"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Completing a Task   (09:57)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 56 - Overdue Task List Assignment:  Part 7</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44663/delete-a-task';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44663"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Delete a Task   (05:13)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 57 - Overdue Task List Assignment:  Part 8</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44665/displaying-information-in-the-detailviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44665"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Displaying Information in the DetailViewController   (06:15)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 58 - Overdue Task List Assignment:  Part 9</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44667/reorder-tasks';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44667"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Reorder Tasks   (05:51)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44668/persisting-the-reorder';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44668"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Persisting the Reorder   (04:04)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 59 - Overdue Task List Assignment:  Part 10</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44670/setting-up-the-editviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44670"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting up the EditViewController   (05:32)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44671/saving-the-editviewcontroller-changes-with-a-delegate';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44671"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Saving the EditViewController Changes with a Delegate   (02:21)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44672/implementing-the-editviewcontroller-delegate';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44672"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing the EditViewController Delegate   (07:12)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44673/implementing-the-detailviewcontroller-delegate';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44673"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing the DetailViewController Delegate   (02:51)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 60 - Overdue Task List Assignment:  Part 11</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44675/make-the-keyboards-go-away';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44675"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Make the Keyboards Go Away!   (05:51)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 61 - Overdue Task List Assignment:  Solution</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44677/overdue-task-list-solution';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44677"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Overdue Task List Solution  </span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 62 - A Deeper Look into Views</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44679/subviews';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44679"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Subviews   (04:42)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44680/difference-between-a-views-frame-and-bounds';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44680"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Difference between a View's Frame and Bounds   (02:21)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44681/a-deeper-look-into-a-views-frame-and-bounds-part-1';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44681"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">A Deeper Look into a View's Frame and Bounds Part 1   (08:37)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44682/a-deeper-look-into-a-views-frame-and-bounds-part-2';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44682"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">A Deeper Look into a View's Frame and Bounds Part 2   (04:13)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 63 - Creating Views Programatically</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44684/adding-a-uiview-programmatically';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44684"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a UIView Programmatically   (07:12)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44685/adding-uibutton-programmatically';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44685"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding UIButton Programmatically   (04:12)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44686/target-action';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44686"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Target Action   (07:23)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 64 - Challenge 13: Custom Views</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44688/the-challenge';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44688"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">The Challenge  </span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44689/custom-views-solution';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44689"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Custom Views Solution   (08:59)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 65 - Autolayout and Constraints</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44691/explore-autolayout';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44691"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Explore Autolayout   (05:23)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44692/demo-autolayouts-part-1';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44692"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Demo Autolayouts Part 1   (11:42)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44693/demo-autolayouts-part-2';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44693"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Demo Autolayouts Part 2   (05:32)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 66 - Further Exploration of Views</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44695/view-controllers-lifecycle';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44695"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">View Controllers Lifecycle   (03:27)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44696/custom-views';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44696"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Custom Views   (06:14)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 67 - Introduction to UIBezierPaths</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44698/drawing-with-uibezierpath-part-1';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44698"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Drawing with UIBezierPath Part 1   (08:31)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44699/drawing-with-uibezierpath-part-2';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44699"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Drawing with UIBezierPath Part 2   (05:40)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 68 - Challenge 14: UIBezierPath</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44701/the-challenge';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44701"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">The Challenge  </span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44702/uibezierpath-solution';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44702"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">UIBezierPath Solution   (06:31)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 69 - Another UIBezierPath</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44704/switch-to-an-ipad-application';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44704"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Switch to an iPad Application   (08:41)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44705/more-uibezierpath';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44705"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">More UIBezierPath  &nbsp;<i class='fa fa-paperclip'></i>  (04:42)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44706/creating-our-path';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44706"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Creating our Path   (07:46)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44708/create-a-pathview-class';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44708"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Create a PathView Class   (03:12)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 70 - Creating a UIBezierPath on our Mountain</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44710/how-storyboard-files-are-saved';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44710"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">How Storyboard Files are Saved   (04:49)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44711/talk-about-code-snippets';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44711"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Talk about Code Snippets   (04:45)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44712/finishing-our-mountain-path';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44712"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Finishing our Mountain Path   (02:03)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 71 - Gesture Recognizers and Screen Interaction</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44714/gesture-recognizers';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44714"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Gesture Recognizers   (10:24)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44715/pan-gesture-recognizers';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44715"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Pan Gesture Recognizers   (03:10)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 72 - Scoring for our MountainPath</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44717/detect-a-uibezierpath-hit';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44717"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Detect a UIBezierPath Hit   (07:15)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44718/nstimer';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44718"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">NSTIMER   (03:13)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44719/adding-a-score';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44719"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a Score   (07:46)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44720/finishing-touches-on-our-maze';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44720"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Finishing Touches on our Maze   (08:34)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 73 - Theory: Memory Management</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44722/memory-management-detour';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44722"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Memory Management Detour   (03:41)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44723/object-ownership-strong-and-weak';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44723"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Object Ownership Strong and Weak   (04:43)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44724/retain-cycle-they-are-bad';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44724"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Retain Cycle they are Bad   (04:30)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 74 - Setting up our New Project</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44726/beginning-a-new-journey';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44726"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Beginning a New Journey   (03:13)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44727/starting-our-new-application-and-the-app-delegate';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44727"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Starting our New Application and the App Delegate   (07:39)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44728/adding-a-storyboard-and-a-uitableviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44728"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a Storyboard and a UITableViewController   (08:38)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 75 - Introduction to CoreData</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44730/core-data-an-initial-light-dusting';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44730"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Core Data an Initial Light Dusting   (03:11)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44731/updating-our-xdatamodel';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44731"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Updating our xdatamodel   (07:32)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 76 - UIAlertView</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44733/adding-a-new-album-with-uialertview';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44733"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a New Album with UIAlertView   (05:23)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44734/uialertviewdelegate';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44734"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">UIAlertViewDelegate   (06:04)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 77 - Our CoreData</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44736/its-alive-creating-our-first-nsmanagedobjectsubclass';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44736"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">It;s Alive! Creating our First NSManagedObjectSubclass   (11:50)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44737/nsmanage-objectsubclass-a-quick-review';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44737"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Nsmanage ObjectSubclass a Quick Review   (03:29)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44738/finally-creating-an-album';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44738"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Finally Creating an Album   (07:09)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 78 - Accessing our Models from CoreData</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44740/querying-our-database-for-objects';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44740"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Querying our Database for Objects   (10:37)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44741/review-accessing-objects-from-our-database';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44741"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Review Accessing Objects from our Database   (02:46)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44742/a-quick-refactor';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44742"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">A Quick Refactor   (08:25)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 79 - UICollectionViewController</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44744/uicollectionviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44744"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">UICollectionViewController   (10:42)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44745/getting-a-photo-on-those-slides';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44745"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Getting a Photo on those Slides  &nbsp;<i class='fa fa-paperclip'></i>  (10:04)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 80 - UIImagePickerController</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44747/uiimagepickercontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44747"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">UIImagePickerController   (07:28)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44748/uiimagepickercontroller-delegate';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44748"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">UIImagePickerController Delegate   (05:31)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44749/grabbing-our-photo-from-uiimagepickercontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44749"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Grabbing our Photo from UIImagePickerController   (05:13)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 81 - A Photo Model</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44751/adjust-our-core-data-model';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44751"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adjust our Core Data Model   (07:20)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44752/filling-out-our-twpicturedatatransformer';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44752"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Filling out our TWPIctureDataTransformer   (06:59)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 82 - Saving a Photo</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44754/creating-and-storing-our-photos';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44754"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Creating and Storing our Photos   (06:53)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44755/implementing-creating-and-storing-the-photos';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44755"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing, Creating, and Storing the Photos   (02:25)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 83 - Further Photo Intergration</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44757/prepare-the-segue-practice';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44757"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Prepare the Segue Practice   (05:00)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44758/querying-the-photos-and-debugging';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44758"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Querying the Photos and Debugging   (08:01)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 84 - Deleting a Photo</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44760/adding-a-photo-detailviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44760"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a Photo DetailViewController   (06:05)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44761/deleting-a-photo-from-core-data';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44761"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Deleting a Photo from Core Data   (08:51)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44762/fixing-the-bug';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44762"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Fixing the Bug   (06:17)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 85 - Preparing for Image Filters</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44764/adding-a-collectionviewcontroller-for-the-filters';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44764"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a CollectionViewController for the Filters   (05:43)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44765/creating-filters';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44765"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Creating Filters   (02:34)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44766/collectionview-datasource-methods';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44766"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">CollectionView DataSource Methods   (07:35)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 86 - Image Filts</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44768/adding-our-filters';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44768"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding our Filters   (12:20)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44769/through-our-filters';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44769"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Through our Filters   (09:14)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44770/saving-our-filters';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44770"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Saving our Filters   (06:12)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 87 - Multithreading</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44772/why-is-our-app-slow';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44772"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Why is our App Slow   (04:53)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44773/gcd-and-threading-overview';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44773"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">GCD and Threading Overview   (05:03)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44774/blocks';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44774"></i>
										</span></center>td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Blocks   (04:52)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 88 - Blocks and Grand Central Dispatch</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44776/creating-a-block-and-implementing-it';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44776"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Creating a Block and Implementing it   (04:58)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44777/gcd-example';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44777"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">GCD Example   (07:21)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44778/fixing-our-bug';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44778"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Fixing our Bug   (03:49)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 89 - Getting Ready for Parse</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44780/install-ruby-and-ruby-gems';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44780"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Install Ruby and Ruby Gems   (08:31)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44781/what-is-cocoapods-and-installation';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44781"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">What is CocoaPods and Installation   (02:27)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44782/sign-up-for-parse';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44782"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Sign Up for Parse   (04:21)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44783/what-is-parse-and-why-use-it';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44783"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">What is Parse and Why use it   (06:31)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44784/installing-parse';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44784"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Installing Parse   (05:51)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44785/installing-parse-the-hard-way';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44785"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Installing Parse The Hard Way   (04:38)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 90 - Testing Parse</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44787/is-parse-working';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44787"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Is Parse Working   (05:01)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44790/testing-parse-storyboard-setup';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44790"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Testing Parse Storyboard Setup   (04:25)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 91 - PFObjects</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44792/creating-pfobjects';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44792"></i>
										span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Creating PFObjects   (03:43)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44793/saving-pfobjects';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44793"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Saving PFObjects   (03:38)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44794/querying-for-the-pfobjects';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44794"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Querying for the PFObjects   (06:11)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 92 - Final Project: Matchedup</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44796/matchedup';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44796"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Matchedup  &nbsp;<i class='fa fa-paperclip'></i>  (07:46)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44797/setting-up-parse';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44797"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting up Parse   (04:21)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44798/sign-up-and-setting-up-facebook';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44798"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Sign up and Setting up Facebook   (04:00)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44799/integrating-facebook';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44799"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Integrating Facebook   (06:58)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44802/installing-facebook-the-hard-way';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44802"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Installing Facebook the Hard Way   (02:47)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 93 - Matchedup: Login Functionality</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44804/login-functionality';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44804"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Login Functionality   (10:18)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44805/pfuser';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44805"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">PFUser   (02:22)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44806/saving-user-information';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44806"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Saving User Information   (11:36)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 94 - Matchedup: The API Response</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44808/a-deeper-look-in-facebooks-api';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44808"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">A Deeper Look in Facebook's API   (02:07)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44809/global-constants';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44809"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Global Constants   (08:34)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44810/implementing-our-constants';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44810"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing Our Constants   (02:37)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44811/prep-to-save-a-photo-creating-constants-and-a-url';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44811"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Prep to Save a Photo Creating Constants and a URL   (07:14)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44812/saving-the-image-with-a-pffile';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44812"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Saving the Image with a PFFile   (07:26)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44813/hitting-the-url';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44813"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Hitting the URL   (07:22)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44814/implementing-nsurlconnection-delegates';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44814"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing NSURLConnection Delegates   (03:20)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44815/what-is-the-user-is-already-logged-in';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44815"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">What is the User is Already Logged in?   (03:57)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44817/adding-a-picture-to-the-profileviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44817"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a Picture to the ProfileViewController   (07:40)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 95 - Matchedup: Next Steps</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44819/wireframes';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44819"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Wireframes  &nbsp;<i class='fa fa-paperclip'></i>  (01:01)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44820/storyboard-refactor';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44820"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Storyboard Refactor   (01:28)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 96 - Matchedup: Adding the ViewController's</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44822/add-a-homeviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44822"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Add a HomeViewController   (10:09)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44823/add-a-settingsviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44823"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Add a SettingsViewController   (08:23)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44824/add-a-editprofileviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44824"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Add a EditProfileViewController   (06:52)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44825/add-a-profileviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44825"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Add a ProfileViewController   (06:33)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44826/refactor-login-view-controller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44826"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Refactor Login View Controller   (07:29)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44827/setting-up-the-homeviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44827"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting up the HomeViewController   (07:57)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 97 - Matchedup: Managing Actions</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44829/downloading-the-home-photo';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44829"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Downloading the Home Photo   (06:50)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44831/updating-the-home-views-information';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44831"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Updating the Home View's Information   (03:06)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44832/loading-the-next-photo';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44832"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Loading the Next Photo   (03:40)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44833/save-a-like';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44833"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Save a Like   (08:30)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44834/save-a-dislike';">
							td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44834"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Save a Dislike   (03:20)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44835/check-for-likes';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44835"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Check for Likes   (03:25)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44836/check-for-dislikes';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44836"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Check for Dislikes   (02:59)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44837/implement-our-helper-methods';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44837"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implement our Helper Methods   (02:07)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44838/doing-a-initial-query-for-likes';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44838"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Doing a Initial Query for Likes   (11:59)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44839/creating-global-constants-for-the-homeviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44839"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Creating Global Constants for the HomeViewController   (05:35)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44840/implementing-constants-in-the-homeviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44840"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing Constants in the HomeViewController   (07:46)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 98 - Matchedup: Managing User Profiles</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44842/creating-a-test-users';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44842"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Creating a Test Users   (12:42)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44843/implementing-the-profileviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44843"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing the ProfileViewController   (07:33)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44844/global-constants-for-the-settings-page';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44844"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Global Constants for the Settings Page   (02:51)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44845/setting-initial-values-and-preparing-the-slider-and-switches';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44845"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting Initial Values and Preparing the Slider and Switches   (05:20)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44846/sliders-and-switch-changes';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44846"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Sliders and Switch Changes   (05:49)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44847/loading-the-editprofileviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44847"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Loading the EditProfileViewController   (03:15)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44848/saving-the-tagline';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44848"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Saving the TagLine   (02:00)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44850/logging-out';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44850"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Logging Out   (02:36)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 99 - Matchedup: Storyboard Setup</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44852/storyboard-setup-match';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44852"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Storyboard Setup Match   (06:52)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44853/storyboard-setup-matches';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44853"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Storyboard Setup Matches   (03:13)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44854/storyboard-setup-chat';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44854"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Storyboard Setup Chat   (06:25)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 100 - Matchedup: Chat Prep</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44856/check-for-users-likes';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44856"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Check for Users Likes   (05:53)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44857/create-a-chatroom';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44857"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Create a ChatRoom   (10:33)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 101 - Matchedup: MatchViewController</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44859/prepping-the-matchviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44859"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Prepping the MatchViewController   (02:51)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44860/implementing-the-matchviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44860"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing the MatchViewController   (05:34)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44861/adding-a-delegate-to-the-matchviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44861"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a Delegate to the MatchViewController   (05:40)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 102 - Matchedup: Chat Setup</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44863/finding-available-chats';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44863"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Finding Available Chats   (07:30)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44864/presenting-available-chats';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44864"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Presenting Available Chats   (08:19)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44865/adding-a-picture-to-the-chat-list';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44865"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a Picture to the Chat List   (06:39)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44866/selecting-a-chatroom';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44866"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Selecting a ChatRoom   (03:27)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44867/prepare-the-chatviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44867"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Prepare the ChatViewController   (03:11)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 103 - Matchedup: Implementing Chats</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44869/getting-started-implementing-chats';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44869"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Getting Started Implementing Chats   (05:29)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44870/didsendtext';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44870"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">didSendText   (05:29)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44871/messagetypeforrowatindexpath';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44871"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">messageTypeForRowAtIndexPath   (02:47)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44872/bubbleimageviewwithtype';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44872"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">bubbleImageViewWithType   (02:29)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44875/additional-methods';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44875"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Additional Methods   (03:11)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44876/optional-methods';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44876"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Optional Methods   (02:03)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44877/required';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44877"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Required   (03:32)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 104 - Matchedup: Check/Refresh Chats</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44879/check-for-chats';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44879"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Check for Chats   (05:29)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44881/refreshing-our-chat';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44881"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Refreshing our Chat   (03:36)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44882/testing-chats';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44882"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Testing Chats   (05:02)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 105 - Matchedup: Settings</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44884/setup-defaults-settings';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44884"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setup Defaults Settings   (07:37)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44885/allow-photo-helper-method';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44885"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Allow Photo Helper Method   (08:27)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44886/implement-the-allow-photo';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44886"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implement the Allow Photo   (04:28)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 106 - Matchedup: Constants</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44888/constants-for-chatroom-and-chat';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44888"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Constants for ChatRoom and Chat   (04:35)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44889/implementing-constants';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44889"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implementing Constants   (05:56)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 107 - Matchedup: Assets</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44891/asset-library';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44891"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Asset Library  &nbsp;<i class='fa fa-paperclip'></i>  (03:01)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44892/setting-a-global-nav-bar';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44892"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting a Global Nav Bar   (03:03)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44893/assets-login-viewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44893"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Assets Login ViewController   (03:37)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44894/asset-home-viewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44894"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Asset Home ViewController   (13:50)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44895/assets-profile-viewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44895"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Assets Profile ViewController   (08:39)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44896/finishing-up-the-profile-viewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44896"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Finishing up the Profile ViewController   (07:49)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44898/assets-matches-viewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44898"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Assets Matches ViewController   (01:23)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44899/update-the-chatviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44899"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Update the ChatViewController   (02:29)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44900/assets-setting-viewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44900"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Assets Setting ViewController   (02:32)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44901/editprofile-view-controller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44901"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">EditProfile View Controller   (07:32)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 108 - Matchedup: Transition</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44903/matchviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44903"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">MatchViewController   (04:46)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44904/create-a-transition-class';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44904"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Create a Transition Class   (03:34)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44905/conform-and-implement-uiviewcontrollertransitioningdelegate';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44905"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Conform and Implement UIViewControllerTransitioningDelegate   (09:14)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 109 - Matchedup: MixPanel</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44907/getting-started-with-mixpanel';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44907"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Getting Started with MixPanel   (02:57)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44909/implement-mixpanel';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44909"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Implement MixPanel   (03:59)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44910/using-mixpanel';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44910"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Using MixPanel   (03:43)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 110 - You did it!</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44912/you-did-it';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44912"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-file-text"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">You did it!  </span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 111 - Requested Topic: MVC Review</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44914/mvc-review-part-1';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44914"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">MVC Review Part 1   (07:56)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44915/mvc-review-part-2';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44915"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">MVC Review Part 2   (07:19)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44916/mvc-review-part-3';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44916"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">MVC Review Part 3   (11:34)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44917/mvc-review-part-4';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44917"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">MVC Review Part 4   (04:47)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 112 - Requested Topic: World Traveler Part 1</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44919/introduction-libraries-and-learning-goals';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44919"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Introduction Libraries and Learning Goals   (05:56)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44920/dependencies-and-libraries';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44920"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Dependencies and Libraries   (07:52)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44921/storyboard-setup';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44921"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Storyboard Setup   (07:52)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44922/model-adding-entities';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44922"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Model Adding Entities   (08:41)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44923/model-adding-relationships';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44923"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Model Adding Relationships   (02:22)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44924/adding-a-primaryattributekey';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44924"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a PrimaryAttributeKey   (05:39)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44925/subclassing-mmrecord-and-keypathforresponseobject';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44925"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Subclassing MMRecord and keyPathForResponseObject   (04:38)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44926/subclassing-afhttpsessionmanager';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44926"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Subclassing AFHTTPSessionManager   (07:32)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44927/foursquare-clientid-and-clientsecret';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44927"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">foursquare ClientID and ClientSecret   (03:33)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44928/imports-and-magicalrecord-setup';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44928"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Imports and MagicalRecord Setup   (04:43)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44930/customizing-tcfoursquaresesssionmanager';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44930"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Customizing TCFourSquareSesssionManager   (06:05)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44931/making-our-first-request';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44931"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Making our First Request   (07:33)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44932/displaying-the-information';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44932"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Displaying the Information   (05:02)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44933/current-location';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44933"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Current Location   (08:39)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44934/venue-setup';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44934"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Venue Setup   (03:02)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44935/setting-up-the-map';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44935"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting up the Map   (06:54)</span>

								
										</td>
					</tr>


												
								</table>
							

						<div class="section">Section 113 - Requested Topic: World Traveler Part 2</div>

						<table class="table table-striped table-bordered table-hover" style="padding:0px;width:100%;">
						
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44937/finishing-up-our-mapviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44937"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Finishing up our MapViewController   (04:04)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44938/updating-the-mapviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44938"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Updating the MapViewController   (02:00)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44939/setting-up-the-directions-viewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44939"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting up the Directions ViewController   (05:14)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44940/location-manager-a-quick-review';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44940"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Location Manager a Quick Review   (07:32)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44941/getting-directions';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44941"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Getting Directions   (05:56)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44942/using-our-directions-method';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44942"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Using our Directions Method   (06:36)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44943/getting-the-route';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44943"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Getting the Route   (05:43)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44944/adding-a-latitude-and-longitude-offset';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44944"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a Latitude and Longitude Offset   (02:59)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44945/drawing-our-overlay';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44945"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Drawing our Overlay   (05:23)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44946/setup-the-directionslistviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44946"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setup the DirectionsListViewController   (04:03)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44947/segue-to-the-directionslistviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44947"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Segue To The DirectionsListViewController   (04:44)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44948/setup-the-list-of-directions';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44948"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setup the List of Directions   (07:17)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44950/adding-a-tableviewheader';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44950"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a TableViewHeader   (03:12)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44951/adding-map-snapshots';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44951"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding Map Snapshots   (09:37)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44952/installing-a-facebook-style-menu-with-mmdrawercontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44952"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Installing a Facebook style Menu with MMDrawerController   (03:36)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44954/adding-a-menuviewcontroller-to-the-storyboard';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44954"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a MenuViewController to the Storyboard   (04:45)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44955/update-the-app-delegate';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44955"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Update the App Delegate   (09:52)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44956/setting-drawer-attributes';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44956"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting Drawer Attributes   (04:56)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44957/adding-animations-to-our-menu';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44957"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding Animations to our Menu   (04:06)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44958/adding-a-menu-button';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44958"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding a Menu Button  &nbsp;<i class='fa fa-paperclip'></i>  (05:24)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44959/setting-up-the-menuviewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44959"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Setting up the MenuViewController   (03:08)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44960/adding-our-listviewcontroller-to-the-menu';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44960"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding our ListViewController to the Menu   (08:57)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44961/selecting-our-menu-item';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44961"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Selecting our Menu Item   (02:09)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44962/adding-some-more-viewcontrollers';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44962"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding some More ViewControllers   (07:56)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44963/adding-our-new-viewcontrollers-to-the-menu-viewcontroller';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44963"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding our new ViewControllers to the Menu ViewController   (05:22)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44964/adding-menu-buttons-to-the-favorite-and-add-venue-viewcontrollers';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44964"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding Menu Buttons to the Favorite and Add Venue ViewControllers   (04:07)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44965/adding-favoriting';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44965"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Adding Favoriting   (05:31)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44968/save-using-magicalrecord';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44968"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Save using MagicalRecord   (02:11)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44969/displaying-our-favorite-venues-with-magical-record';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44969"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Displaying our Favorite Venues with Magical Record   (07:29)</span>

								
										</td>
					</tr>


					
						<tr class="lecture_tr" onClick="window.location.href='http://bitfountain.io/lecture/44970/creating-our-a-custom-venue-with-magical-record';">
							<td style="border-right:0px; padding-top:2px;padding-bottom:2px;border-right-width:0px !important;margin-left:-5px;padding:0px;padding-left:10px;padding-right:0px;width:30px;">
							<center>
							<span style="font-size:24px;color:#34495e;">
																											<i class="fa fa-circle-o" id="circle_44970"></i>
										</span></center></td><td style="margin-left:-5px;padding-left:15px;border-left-width:0px !important;"><span style="font-size:14px;"><i class="fa fa-youtube-play"></i>&nbsp;</span> 

								<span class="lecture" style="font-size:16px;">Creating our a custom Venue with Magical Record   (06:18)</span>

								
										</td>
					</tr>


						</table>

			
		</div>
		</div>

</div>	</div>
	<script type="text/javascript">
	
	var isSidebar = 0;
	
	$( window ).resize(function() {

		var width = $( window ).width();

		if (width>=900)
		{
		$("#course_sidebar").css("display","inline-block");
		$("#main_content").css("display","block");
		}
		if (width<900)
		{
			if (isSidebar!=1)
			{
				$("#course_sidebar").css("display","none");
			}
			else
			{
				$("#main_content").css("display","none");
			}
		}
	});
	
	function toggleMenu()
	{
		if (isSidebar==0)
		{
			isSidebar = 1;
			$("#course_sidebar").css("display","inline-block");
						$("#course_sidebar").css("margin-top","40px");
						$("#main_content").css("display","none");
			//$("#course_lecture_footer").css("display","none");
			//repositionMenu();
		}
		else
		{
			isSidebar = 0;
			$("#course_sidebar").css("display","none");
						//$("#course_lecture_footer").css("display","block");
						$("#course_sidebar").css("margin-top","0px");
						$("#main_content").css("display","block");
		}
		//$("#course_sidebar").css('')
	}
	
	
	var active = 0;
var destinations = new Array();
destinations[0] = "course_cur.php";
destinations[1] = "instructor.php";
destinations[2] = "write_review.php";
	function navigate(destination){
			$("#main_content").html("<center><p><br/><img src='http://bitfountain.io/images/ajaxloader2.gif' /><br /><br /></center>");
		$("#main_content").load("http://bitfountain.io/"+destinations[destination]+"?courseid=1935");
	
		var oldDiv = "#button_"+active;
		active = destination;

		var newDiv = "#button_"+destination;

		//$(oldDiv).css("background-color","#f8f8f8");
		//$(newDiv).css("background-color","#ffffff");
		$(oldDiv).removeClass("menu_maindiv_active");
		$(newDiv).addClass("menu_maindiv_active");
	
		var width = $( window ).width();
		if (width<=900 && isSidebar==1)
		{
			toggleMenu();
		}
	
	
	}
	</script>
	"""
    links = get_all_links(page)
    videos = []
    for l in links:
        links2 = get_all_links2(l)
    videos.append(links2)

SMRequirementsGathering/dashboard_data/
In this folder:

==this file, readme.txt==
Written by Katie

==generateDashboardData.py==
Steps from the code annotations:
1. Get the results from the endpoint
2. Read the CSV output from the endpoint
   #vectorize the hashtags
   #get timestamps 
   #populate the user_tag_dict
3. Write out the timestamps file for the static demo
4. Write out mallet output to static demo
5. Filter out the top 20 users by weighted entropy for a list of hashtags
	(# of times user mentioned all hashtags) * (log_2 [counted # of 
	hashtags they used on the list])
	Write out the co-occurence matrix file
   #do the scoring and filtering
   #write it out to the json file

Input: SPARQL query and endpoint URL are hardcoded
Output: JSON dump of mallet results

==hashtag_list.txt==
Not yet sure where these are from? (generated or selected manually)

==The files in dashboard_data/output==
- mallet_output_wrapper.txt
- matrix_co_tag_user.json
- timestamps.js
appear to be the same as the ones at /static_demo/input/
with the same names.

==dashboard_data/mallet==
- run_mallet.sh, the script called in generateDashboardData.py
Takes as input:
- hashtags.mallet, input for topic modeling(?)
- vectors subdirectory, input for the script
Produces output:
- output.txt, contains the output of the mallet script(?)
- keys.txt, also output by the mallet script???

* this script is set up to run on Zach's machine
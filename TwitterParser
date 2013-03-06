#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <map>
#include <math.h>
#include <time.h>
#include <fstream>
#include "tdd.h"

using namespace std;

ifstream input;
ofstream output;
TwitterData TwitterData_Object;
UserMentions UserMentions_Struct;
Hashtags Hashtags_Struct;
URLs URLs_Struct;
CreatedAt CreatedAt_Struct;

vector<TwitterData> TwitterData_Vector;
vector<UserMentions> UserMentions_Vector;
vector<Hashtags> Hashtags_Vector;
vector<URLs> URLs_Vector;
vector<CreatedAt> CreatedAt_Vector;

void ReadTwitterData()
{
  int counter = 0;
	string a;
//	input.open("1 OriginalData/CoEMS.txt");
	input.open("1 OriginalData/2BeeRdy.txt");
	while(input>>a)
	{		
		TwitterData_Object.setter_mark(counter);
//		if(a == "\"completed_in\":")
// 		{
// 			string b;
// 			input>>b;
// 			TwitterData_Object.setter_completed_in(b);
// 		}
//		else if(a == "\"max_id_str\":")
// 		{
// 			string b;
// 			input>>b;
// 			TwitterData_Object.setter_max_id(b);
// 		}
//		else if(a == "\"since_id_str\":")
// 		{
// 			string b;
// 			input>>b;
// 			TwitterData_Object.setter_since_id(b);
// 		}
//		else if(a == "\"refresh_url\":")
// 		{
// 			string b;
// 			input>>b;
// 			TwitterData_Object.setter_refresh_url(b);
// 		}
//		else if(a == "\"to_user_name\":")
		if(a == "\"to_user_name\":")
		{
			string tempString1;
			input>>tempString1;
			if(tempString1 == "null,")
				TwitterData_Object.setter_to_user_name("null");
			else
			{
				string tempString2;
				tempString2 = tempString1;
				while(input>>tempString1)
				{
					if(tempString1 == "\"to_user_id_str\":")
 	 					break;
 	 				tempString2=tempString2+" "+tempString1;					
				}
				TwitterData_Object.setter_to_user_name(tempString2);
				input>>tempString1;
				TwitterData_Object.setter_to_user_id(tempString1);
			}
			input>>tempString1;
			if(tempString1 == "\"to_user_id_str\":")
			{
				input>>tempString1;
			}
			input>>tempString1;
			if(tempString1 == "\"profile_image_url_https\":")
			{
				input>>tempString1;
			}
			input>>tempString1;
			if(tempString1 == "\"from_user_id_str\":")
			{
				input>>tempString1;
				TwitterData_Object.setter_from_user_id(tempString1);
			}
			input>>tempString1;
 			if(tempString1 == "\"source\":")
 			{
				string tempString2;
 				input>>tempString1;
				input>>tempString2;
//				TwitterData_Object.setter_source(tempString1+tempString2);
 			}
			input>>tempString1;
			if(tempString1 == "\"text\":")
			{
				string tempString3, tempString4;
				while(input>>tempString1)
				{
					if(tempString1 == "\"from_user_name\":")
						break;
					tempString3=tempString3+" "+tempString1;
				}
				TwitterData_Object.setter_text(tempString3);
				while(input>>tempString1)
				{
					if(tempString1 == "\"profile_image_url\":")
						break;
					tempString4 = tempString4+" "+tempString1;
				}
				TwitterData_Object.setter_from_user_name(tempString4);

			}	
			if(tempString1 == "\"profile_image_url\":")
			{
				input>>tempString1;
				TwitterData_Object.setter_profile_image_url(tempString1);
			}
			input>>tempString1;
 			if(tempString1 == "\"id\":")
 			{
 				input>>tempString1;
//				TwitterData_Object.setter_id(tempString1);
 			}
			input>>tempString1;
			if(tempString1 == "\"to_user\":")
			{
			    input>>tempString1;
			    if(tempString1 == "null,")
			    	TwitterData_Object.setter_to_user("null");
			    else
			    {
			    	string tempString4;
			    	tempString4 = tempString1;
			    	while(input>>tempString1)
			    	{
			    		if(tempString1 == "\"entities\":")
 	 		    			break;
 	 		    		tempString4=tempString4+" "+tempString1;					
			    	}
			    	TwitterData_Object.setter_to_user(tempString4);
			    }
			}
		}
		if(a == "\"user_mentions\":")
		{
			string tempString1;
			char tempChar1;
			double tempDouble1;
			int tempInt1;			
			while(input>>tempString1 && tempString1 != "\"hashtags\":")
			{
				UserMentions_Struct.mark = counter;
				if(tempString1 == "\"id\":")
				{
					input>>tempDouble1;
					UserMentions_Struct.UserId = tempDouble1;
				}
				if(tempString1 == "\"indices\":")
				{
					input>>tempChar1;
					input>>tempInt1;
					UserMentions_Struct.IndiceStart = tempInt1;
					input>>tempChar1;
					input>>tempInt1;
					UserMentions_Struct.IndiceEnd = tempInt1;
					input>>tempChar1;
				}
				if(tempString1 == "\"screen_name\":")
				{
					input>>tempString1;
					UserMentions_Struct.ScreenName = tempString1;
				}
				if(tempString1 == "\"name\":")
				{
					string tempString2;
					while(input>>tempString1)
					{
						if(tempString1 == "}" || tempString1 == "},")
							break;
						tempString2 = tempString2+" "+tempString1;
					}
					UserMentions_Struct.Name = tempString2;
					UserMentions_Vector.push_back(UserMentions_Struct);
				}
			}
			while(input>>tempString1 && tempString1 != "\"urls\":")
			{
				Hashtags_Struct.mark = counter;
				if(tempString1 == "\"indices\":")
				{
					input>>tempChar1;
					input>>tempInt1;
					Hashtags_Struct.IndiceStart = tempInt1;
					input>>tempChar1;
					input>>tempInt1;
					Hashtags_Struct.IndiceEnd = tempInt1;
					input>>tempChar1;
				}
				if(tempString1 == "\"text\":")
				{
					input>>tempString1;
					Hashtags_Struct.HashtagName = tempString1;
					Hashtags_Vector.push_back(Hashtags_Struct);
				}
			}
			while(input>>tempString1 && tempString1 != "\"id_str\":")
			{
				URLs_Struct.mark = counter;
				if(tempString1 == "\"url\":")
				{
					input>>tempString1;
					URLs_Struct.url = tempString1;
				}
				if(tempString1 == "\"indices\":")
				{
					input>>tempChar1;
					input>>tempInt1;
					URLs_Struct.IndiceStart = tempInt1;
					input>>tempChar1;
					input>>tempInt1;
					URLs_Struct.IndiceEnd = tempInt1;
					input>>tempChar1;
				}
				if(tempString1 == "\"expanded_url\":")
				{
					input>>tempString1;
					URLs_Struct.ExpendURL = tempString1;
				}
				if(tempString1 == "\"display_url\":")
				{
					input>>tempString1;
					URLs_Struct.DisplayURL = tempString1;
					URLs_Vector.push_back(URLs_Struct);
				}
			}
		}
		if(a == "\"from_user\":")
		{
			input>>a;
			TwitterData_Object.setter_from_user(a);
		}
//		if(a == "\"geo\":")
//		{
//			input>>a;
//			TwitterData_Object.setter_geo(a);
//		}
		if(a == "\"created_at\":")
		{
			int tempInt1;
			char tempChar1;
			CreatedAt_Struct.mark = counter;
			input>>a;
			CreatedAt_Struct.weekday = a;
			input>>tempInt1;
			CreatedAt_Struct.day = tempInt1;
			input>>a;
			CreatedAt_Struct.month = a;
			input>>tempInt1;
			CreatedAt_Struct.year = tempInt1;
			input>>tempInt1;
			CreatedAt_Struct.hour = tempInt1;
			input>>tempChar1;
			input>>tempInt1;
			CreatedAt_Struct.minute = tempInt1;
			input>>tempChar1;
			input>>tempInt1;
			CreatedAt_Struct.second = tempInt1;
			input>>a;
			CreatedAt_Struct.timezone = a;
			CreatedAt_Vector.push_back(CreatedAt_Struct);
		}
		if(a == "\"metadata\":")
		{
			TwitterData_Vector.push_back(TwitterData_Object);
			counter++;
		}
	}

	input.close();
}
void WriteFromUser()
{
	output.open("2 OutputData/from_user.txt");
	for(int i = 0; i<TwitterData_Vector.size(); i++)
	{
		output<<TwitterData_Vector[i].getter_mark()<<" "<<TwitterData_Vector[i].getter_from_user()<<endl;
	}
	output.close();
}
void WriteFromUserName()
{
	output.open("2 OutputData/from_user_name.txt");
	for(int i = 0; i<TwitterData_Vector.size(); i++)
	{
		output<<TwitterData_Vector[i].getter_mark()<<" "<<TwitterData_Vector[i].getter_from_user_name()<<endl;
	}
	output.close();
}
void WriteFromUserId()
{
	output.open("2 OutputData/from_user_id.txt");
	for(int i = 0; i<TwitterData_Vector.size(); i++)
	{
		output<<TwitterData_Vector[i].getter_mark()<<" "<<TwitterData_Vector[i].getter_from_user_id()<<endl;
	}
	output.close();
}
void WriteTitterText()
{
	output.open("2 OutputData/twitter_text.txt");
	for(int i = 0; i<TwitterData_Vector.size(); i++)
	{
		output<<TwitterData_Vector[i].getter_mark()<<" "<<TwitterData_Vector[i].getter_text()<<endl;
	}
	output.close();
}
void WriteUserMentions()
{
	output.open("2 OutputData/user_mentions.txt");
	for(int i = 0; i<UserMentions_Vector.size(); i++)
	{
		output<<UserMentions_Vector[i].mark<<" "<<UserMentions_Vector[i].Name<<" "<<UserMentions_Vector[i].ScreenName<<" "<<UserMentions_Vector[i].UserId<<endl;
	}
	output.close();
}
void WriteHashtags()
{
	output.open("2 OutputData/hashtags.txt");
	for(int i = 0; i<Hashtags_Vector.size(); i++)
	{
		output<<Hashtags_Vector[i].mark<<" "<<Hashtags_Vector[i].HashtagName<<endl;
	}
	output.close();
}
void WriteUrls()
{
	output.open("2 OutputData/urls.txt");
	for(int i = 0; i<URLs_Vector.size(); i++)
	{
		output<<URLs_Vector[i].mark<<" "<<URLs_Vector[i].url<<" "<<URLs_Vector[i].DisplayURL<<" "<<URLs_Vector[i].ExpendURL<<endl;
	}
	output.close();
}

int main()
{

	ReadTwitterData();
	WriteFromUser();
	WriteFromUserName();
	WriteFromUserId();
	WriteTitterText();
	WriteUserMentions();
	WriteHashtags();
	WriteUrls();

	return 0;
}

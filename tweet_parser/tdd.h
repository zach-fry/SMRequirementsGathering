#ifndef TDD_H
#define TDD_H

#include <string>

using namespace std;

struct UserMentions
{
  double UserId;
	int IndiceStart, IndiceEnd;
	string ScreenName;
	string Name;
	int mark;
};

struct Hashtags
{
	int IndiceStart, IndiceEnd;
	string HashtagName;
	int mark;
};

struct URLs
{
	string url;
	int IndiceStart, IndiceEnd;
	string ExpendURL;
	string DisplayURL;
	int mark;
};

struct CreatedAt
{
	string weekday;
	int day;
	string month;
	int year;
	int hour;
	int minute;
	int second;
	string timezone;	
	int mark;
};

class TwitterData
{
private:
	double mark;
//	string completed_in;
//	string max_id;
// 	string next_page;
//	string page;
//	string query;
//	string refresh_url;
//	string results_per_page;
//	string since_id;
 
	string from_user;
	string from_user_id;
	string from_user_name;
// 	string geo;
//	string id;
//	string iso_language_code;
//	string result_type;
	string profile_image_url;
//	string profile_image_url_https;
//	string source;
	string text;
	string to_user;
	string to_user_id;
//	string to_user_id_str;
	string to_user_name;

//	string in_reply_to_status_id;

public:
	TwitterData()
	{}
	~TwitterData()
	{}

	// mark each twitter
	void setter_mark(double i)
	{mark = i;}
	double getter_mark()
	{return mark;}

//	void setter_completed_in (string a)
//	{completed_in = a;}
//	string getter_completed_in ()
//	{return completed_in;}

//	void setter_max_id (string a)
//	{max_id = a;}
//	string getter_max_id ()
//	{return max_id;}

//	void setter_next_page (string a)
//	{next_page = a;}
//	string getter_next_page ()
//	{return next_page;}
	
//	void setter_page (string a)
//	{page = a;}
//	string getter_page ()
//	{return page;}
	
//	void setter_query (string a)
//	{query = a;}
//	string getter_query ()
//	{return query;}
	
//	void setter_refresh_url (string a)
//	{refresh_url = a;}
//	string getter_refresh_url ()
//	{return refresh_url;}

//	void setter_results_per_page(string a)
//	{results_per_page = a;}
//	string getter_results_per_page()
//	{return results_per_page;}

//	void setter_since_id(string a)
//	{since_id = a;}
//	string getter_since_id()
//	{return since_id;}

	void setter_from_user (string a)
	{from_user = a;}
	string getter_from_user()
	{return from_user;}

	void setter_from_user_id (string a)
	{from_user_id = a;}
	string getter_from_user_id()
	{return from_user_id;}

	void setter_from_user_name (string a)
	{from_user_name = a;}
	string getter_from_user_name()
	{return from_user_name;}

//	void setter_geo (string a)
//	{geo = a;}
//	string getter_geo()
//	{return geo;}

//	void setter_id (string a)
//	{id = a;}
//	string getter_id()
//	{return id;}

//	void setter_iso_language_code (string a)
//	{iso_language_code = a;}
//	string getter_iso_language_code()
//	{return iso_language_code;}

//	void setter_result_type (string a)
//	{result_type = a;}
//	string getter_result_type()
//	{return result_type;}

	void setter_profile_image_url (string a)
	{profile_image_url = a;}
	string getter_profile_image_url()
	{return profile_image_url;}

//	void setter_profile_image_url_https (string a)
//	{profile_image_url_https = a;}
//	string getter_profile_image_url_https()
//	{return profile_image_url_https;}

//	void setter_source (string a)
//	{source = a;}
//	string getter_source()
//	{return source;}

	void setter_text (string a)
	{text = a;}
	string getter_text()
	{return text;}

	void setter_to_user (string a)
	{to_user = a;}
	string getter_to_user()
	{return to_user;}

	void setter_to_user_id (string a)
	{to_user_id = a;}
	string getter_to_user_id()
	{return to_user_id;}

//	void setter_to_user_id_str (string a)
//	{to_user_id_str = a;}
//	string getter_to_user_id_str()
//	{return to_user_id_str;}

	void setter_to_user_name (string a)
	{to_user_name = a;}
	string getter_to_user_name()
	{return to_user_name;}

//	void setter_in_reply_to_status_id (string a)
//	{in_reply_to_status_id = a;}
//	string getter_in_reply_to_status_id()
//	{return in_reply_to_status_id;}

};


#endif

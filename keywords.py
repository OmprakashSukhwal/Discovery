from locators import locators
from common.global_lib import Global
import csv
from robot.libraries.BuiltIn import BuiltIn
__all__ = ['Keywords']

class Keywords(Global):


    def go_to_discovery_home_page(self):
        self.open_browser("https://go.discovery.com/")

    def go_to_footer(self):
        self.click_element(locators.footer)

    def add_to_favourite(self):
        self.wait_until_page_contains_element(locators.search_results, 30)
        count = self.get_matching_xpath_count(locators.search_result)
        print count
        search_result_shows = []
        for index in range(1,int(count)+1):
            print "a",index
            name = self.get_element_attribute(locators.search_result.replace('%s', index), "href")
            print name
            search_result_shows.append()
            # self.click_element(show)
            try:
                self.click_element(locators.add_to_fav)
            except:
                pass
        print search_result_shows

    def search_show(self,show_keyword):
        self.click_element(locators.search_icon)
        self.input_text(locators.search_input, show_keyword)
        self.click_element(locators.view_all_results)

    def go_to_my_videos(self):
        self.click_element(locators.menu_link)
        self.click_element(locators.my_videos)

    def move_to_popular_shows_dot_pager(self):
        self.click_element(locators.popular_show_dot_pager)

    def go_to_last_popular_show(self):
        count = self.get_matching_xpath_count(locators.all_popular_shows_explore_btn)
        for i in range(int(count)):
            try:
                self.click_element(locators.right_arrow)
            except:
                break

    def explore_the_show(self):
        count = self.get_matching_xpath_count(locators.all_popular_shows_explore_btn)
        self.click_element(locators.explore_btn.replace("%s",count))

    def show_more_episode(self):
        while True:
            try:
                self.click_element(locators.show_more_button)
            except:
                break

    def get_all_episodes_title_and_time(self):
        count = self.get_matching_xpath_count(locators.episodes)
        titles = []
        duration = []
        title_duration_dict = {}
        for index in range(1,int(count)+1):
            titles.append(self.get_text(locators.episode_titles.replace('%s',str(index))))
            duration.append(self.get_text(locators.episode_durations.replace("%s", str(index))))
        title_duration_dict.update(zip(titles,duration))
        return title_duration_dict

    def export_title_duration_to_file(self,title_duration_dict):
        with open('output.csv', 'wb') as output:
            writer = csv.writer(output)
            for key, value in title_duration_dict.iteritems():
                writer.writerow([key, value])

    def click_shows(self):
        self.click_element(locators.shows)

    def click_see_all_shows(self):
        self.click_shows()
        self.click_element(locators.see_all_shows)

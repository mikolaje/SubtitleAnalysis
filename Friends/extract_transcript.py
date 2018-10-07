# coding=u8
import re


def filter_sentence(season, episode):
    with open('subtitles/s%s/Friends.S%sE%s.chs&eng.ass' % (season, season, episode), 'r', encoding='u8') as rf, \
            open('filtered_subtitles/s%s/FriendsS%sE%s.txt' % (season, season, episode), 'w', encoding='u8') as wf:
        for line in rf:

            match_ch = re.search(r"8000&\\b0\}(.*?)\{\\", line)
            match_en = re.search(r"C0&\\b0\}(.*?)\{\\", line)
            match_en = re.search(r"C0&\\b0\}(.*)", line)  # for season 09
            if match_en and match_ch:
                chinese = match_ch.group(1)
                english = match_en.group(1)
                print(english)

                output_line = chinese + '\b0\b1\b2---' + english + '\n'
                wf.write(output_line)
                print(output_line)



if __name__=='__main__':

    episode_list = [format(i, '02d') for i in range(1, 24)]
    for each in episode_list:
        filter_sentence('08', each)

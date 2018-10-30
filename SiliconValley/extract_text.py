# coding=u8
import re
import shutil
import glob


def extract(season, episode):
    with open('subtitles/S%s/Silicon.Valley.S%sE%s.srt' % (season, season, episode), 'r', encoding='u8') as rf, \
        open('filtered_subtitles/S%s/SiliconValleyS%sE%s.txt' % (season, season, episode), 'w', encoding='u8') as wf:
        for line in rf:
            line = line.strip()
            match = re.search('^\d+$', line)
            if (match == None) and ('-->' not in line) and (len(line) > 0):
                if re.search(r'[a-zA-Z]', line):
                    wf.write(line + '\n')



def cat_sub_season(season):

    outfilename = "filtered_subtitles/S%s/S%s_all.txt" % (season, season)
    with open(outfilename, 'wb') as outfile:
        for filename in glob.glob('filtered_subtitles/S%s/*.txt' % season):
            if filename == outfilename:
                # don't want to copy the output into the output
                continue
            with open(filename, 'rb') as readfile:
                shutil.copyfileobj(readfile, outfile)





if __name__ == '__main__':
    episode_list = [format(i, '02d') for i in range(1, 11)]
    cat_sub_season('04')
    #for episode in episode_list:
        #extract('04', episode)


# coding=u8
import re
import glob, os
import codecs
import io
import shutil


def convert2utf8(path):
    print(path)
    with io.open(path, 'r', encoding='utf8', errors='ignore') as f:
        text = f.read()
    # process Unicode text
    with io.open(path, 'w', encoding='utf8') as f:
        f.write(text)


def extract(season):
    for file in os.listdir("subtitles/S%s" % season):
        if file.endswith(".srt"):
            path = os.path.join("subtitles/S%s" % season, file)
            #convert2utf8(path)

            print(path)
            match = re.search(r'e(\d{2})', path.lower())
            episode = match.group(1)
            with open(path, 'r', encoding='utf-8') as rf,\
                open('filtered_subtitles/S%s/S%sE%s.txt' % (season, season, episode), 'w', encoding='utf-8') as wf:
                for line in rf:
                    line = line.strip()
                    match = re.search('^\d+$', line)
                    match2 = re.search(r'www\..*\.(com|net|tv|org|es)', line)
                    if (match is None) and ('-->' not in line) and (len(line) > 0) and (match2 is None):
                        line = line.replace('- ', ' ').strip()
                        line = re.sub(r'<font .*?>', '', line)
                        line = line.replace('</i>', '').replace('<i>', '')
                        print(line)
                        wf.write(line + '\n')


def cat_sub_season(season):
    path_list = []
    for file in os.listdir("filtered_subtitles/S%s" % season):
        if file.endswith(".txt"):
            path = os.path.join("filtered_subtitles/S%s" % season, file)
            if 'all' not in path:
                path_list.append(path)


    outfilename = "filtered_subtitles/S%s/S%s_all.txt" % (season, season)
    print(path_list)
    with open(outfilename, 'w', encoding='utf-8') as outfile:
        for fname in path_list:
            with open(fname, encoding='utf-8') as infile:
                outfile.write(infile.read())


if __name__ == '__main__':
    season = '04'
    extract(season)
    cat_sub_season(season)


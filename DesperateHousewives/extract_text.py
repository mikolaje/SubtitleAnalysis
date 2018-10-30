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


def cat_sub_season(season):

    outfilename = "filtered_subtitles/S%s/S%s_all.txt" % (season, season)
    with open(outfilename, 'wb') as outfile:
        for filename in glob.glob('filtered_subtitles/S%s/*.txt' % season):
            if filename == outfilename:
                # don't want to copy the output into the output
                continue
            with open(filename, 'rb') as readfile:
                shutil.copyfileobj(readfile, outfile)


def extract(season):
    for file in os.listdir("subtitles/S%s" % season):
        if file.endswith(".srt"):
            path = os.path.join("subtitles/S%s" % season, file)
            convert2utf8(path)


            with open(path, 'r', encoding='utf-8') as rf,\
                open('filtered_subtitles/S%s/S%s_all.txt' % (season, season), 'w', encoding='utf-8') as wf:
                for line in rf:
                    line = line.strip()
                    match = re.search('^\d+$', line)
                    if (match is None) and ('-->' not in line) and (len(line) > 0):
                        line = line.replace('- ', ' ').strip()
                        line = re.sub(r'<font .*?>', '', line)
                        line = line.replace('</i>', '').replace('<i>', '')
                        wf.write(line + '\n')




if __name__ == '__main__':
    extract('08')


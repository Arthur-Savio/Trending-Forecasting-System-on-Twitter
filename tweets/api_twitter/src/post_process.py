import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


class PostProcessTweets:
    #Class to generate graphics
    def __init__(self, count_good, count_bad, sentiment_datas):
        self.sentiment_datas = sentiment_datas
        self.count_good = count_good
        self.count_bad = count_bad

    def generate_all_graphics(self):
        self.sentiment_graphic()
        self.good_words_graphic()
        self.bad_words_graphic()

    def sentiment_graphic(self):
        #Graphic generated in the form of pizza to quantify the feelings of each tweet.

        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
        labels = ['Bad', 'Medium', 'Good']
        data = self.sentiment_datas

        wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40, 
                                colors=['red', 'lavender', 'blue'])

        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
        bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1)/2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(labels[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                        horizontalalignment=horizontalalignment, **kw)

        ax.set_title("Sentiment Analysis")
        plt.savefig('web/src/assets/img/sentiment.png')
        plt.clf()
        plt.close()

    def good_words_graphic(self):
        #Gŕafico in bars to quantify the most common good words.

        plt.barh(list(self.count_good.keys()), list(self.count_good.values()),  color='#007FFF')
        plt.savefig('web/src/assets/img/good.png')
        plt.clf()
        plt.close()

    def bad_words_graphic(self):
        #Gŕafico in bars to quantify the most common bad words.

        plt.barh(list(self.count_bad.keys()), list(self.count_bad.values()), color='#FF0000')
        plt.savefig('web/src/assets/img/bad.png')
        plt.clf()
        plt.close()

'''
@author Zach Fry (fryz)
@date 2/11/2013
'''

import json
import codecs

page_pt1 = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Test Cloud</title>
        <script type="text/javascript" src="d3v3/d3.v3.js"></script>
        <script type="text/javascript" src="jquery/jquery-1.9.1.js"></script>
        <script type="text/javascript" src="d3-cloud-master/d3.layout.cloud.js"></script>
    </head>
    <body>
    <div id="wordcloud"></div>
        
        <script type="text/javascript">
        // Based on http://www.jasondavies.com/wordcloud 
        function D3WordCloud(words, newcfg){
            var cfg = {width: 300,
                height: 300,
                font: "sans-serif",
                minsize: 10,
                maxsize: 100,
                wordOrientation: "random",
                color: "black",
                stopwords: ["of", "the", "a", "or", "to", "and", "for", "at", "with", "without", "in", "from", "is", "are", "were", "was", "this", "that", "these", "those", "in", "on"]
            };
            for(i in newcfg){
                cfg[i] = newcfg[i];
            }
            var countingWords = {};
            var totalWords = new Array();
  
            if(!cfg.count){
                for(i in words){
                    var d = words[i].replace(/[()\.]/gi, "");
                    if(cfg.stopwords.indexOf(d)<0){
                        if(countingWords[d] != undefined){ 
                                countingWords[d] += 1
                        }else{
                            countingWords[d] = 1
                        }
                    }
                }
                for(i in countingWords){
                    totalWords.push({name: i, total: countingWords[i]});
                }  
            }else{
                totalWords = words;
            }
            var maxValue = Math.max.apply(Math, totalWords.map(function(d){return d.total;}));
            var wordLinks = new Array();
            for(i in totalWords){
                wordLinks[totalWords[i].name] = totalWords[i].link || undefined;
            }
            d3.layout.cloud().size([cfg.width, cfg.height])
                .words(totalWords.map(function(d) {
                    return {text: d.name, size: parseInt(cfg.minsize + (cfg.maxsize-cfg.minsize)*(d.total/maxValue))};
                }))
                .rotate(function() { var x=~~(Math.random() * 2) * 90; if(cfg.wordOrientation == "horizontal"){x = 0;}if(cfg.wordOrientation == "vertical"){x = 90;} return x; })
                .padding(1)
                .font("arial")
                .fontSize(function(d) { return d.size; })
                .on("end", draw)
                .start();

            function draw(words) {
                var svg = d3.select("#wordcloud").append("svg");
    
                var g = svg.attr("width", cfg.width)
                    .attr("height", cfg.height).append("g")
                    .attr("transform", "translate("+cfg.width/2+","+cfg.height/2+")");
        
                    g.selectAll("text").data(words)
                .enter().append("a").attr("xlink:href", function(d){return wordLinks[d.text]}).append("text")
                    .style("font-family", cfg.font)
                    .style("font-size", function(d) { return d.size + "px"; })
                    .style("fill", cfg.color)
                    .attr("text-anchor", "middle")
                    .attr("transform", function(d) {
                        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                    })
                    .text(function(d) { return d.text; });
        
            }
        }
        var options = {"width":"580","height":"500","color":"steelblue","radius":10,"count":true,"wordOrientation":"horizontal"};
'''

page_pt2 = '''
            D3WordCloud(words, options);
        </script>
    </body>
</html>
'''



f = codecs.open('/home/fryz/twitter_crawler/stats/hashtags.counts', 'r', 'utf8')
words = []
for line in f:
    word,freq = line.strip().split('\t')
    d = {}
    d["name"] = word
    d["total"] = freq
    d["link"] = ""
    words.append(d)
f.close()

words = json.dumps(words)
page_mid = '\n\t\tvar words="%s";\n'%words

f = open('./testcloud.html', 'w')
f.write(page_pt1+page_mid+page_pt2)
f.close()



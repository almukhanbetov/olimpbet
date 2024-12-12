from bs4 import BeautifulSoup
from requests_html import HTMLSession
url = "https://olimpbet.kz/betting/index.php?page=line&action=2&sel[]=8337829"
session = HTMLSession()
res = session.get(url)
soup = BeautifulSoup(res.html.html, 'html.parser')
html_content = """
<tr>
    <td colspan="2">
        <div class="tab" id="odd81256128" data-match-id="81256128" data-match-count="0" data-cont="0" data-champ="7803344" data-sportid="1">
            <nobr>
                <span class="googleStatIssue">
                    <span class="googleStatIssueName">П1</span> -&nbsp;&nbsp;
                    <span id="koefs_idari_3b" class="bet_sel koefs" data-cnt="1" data-select="idari_3b" data-legacy="idari_3b" data-v1="5.94" data-v2="1" data-v3="1" data-match="81256128" data-id="idari_3b" data-live="b1">
                        <b class="value_js"><span id="googleStatKef">5.94</span></b>
                    </span>
                </span>
                &nbsp;
            </nobr>
            <nobr>
                <span class="googleStatIssue">
                    <span class="googleStatIssueName">Х</span> -&nbsp;&nbsp;
                    <span id="koefs_idari_3b" class="bet_sel koefs" data-cnt="1" data-select="idari_3b" data-legacy="idari_3b" data-v1="4.55" data-v2="1" data-v3="1" data-match="81256128" data-id="idari_3b" data-live="b1">
                        <b class="value_js"><span id="googleStatKef">4.55</span></b>
                    </span>
                </span>
                &nbsp;
            </nobr>
             <nobr>
                <span class="googleStatIssue">
                    <span class="googleStatIssueName">П2</span> -&nbsp;&nbsp;
                    <span id="koefs_idari_3b" class="bet_sel koefs" data-cnt="1" data-select="idari_3b" data-legacy="idari_3b" data-v1="1.53" data-v2="1" data-v3="1" data-match="81256128" data-id="idari_3b" data-live="b1">
                        <b class="value_js"><span id="googleStatKef">1.53</span></b>
                    </span>
                    <!--b>1.53</b-->
                </span>
                &nbsp;
            </nobr>
             <nobr>
                <span class="googleStatIssue">
                    <span class="googleStatIssueName">1Х</span> -&nbsp;&nbsp;
                    <span id="koefs_idari_3b" class="bet_sel koefs" data-cnt="1" data-select="idari_3b" data-legacy="idari_3b" data-v1="2.55" data-v2="1" data-v3="1" data-match="81256128" data-id="idari_3b" data-live="b1">
                        <b class="value_js"><span id="googleStatKef">2.55</span></b>
                    </span>
                    <!--b>2.55</b-->
                </span>
                &nbsp;
            </nobr>
            <nobr>
                <span class="googleStatIssue">
                    <span class="googleStatIssueName">12</span> -&nbsp;&nbsp;
                    <span id="koefs_idari_3b" class="bet_sel koefs" data-cnt="1" data-select="idari_3b" data-legacy="idari_3b" data-v1="1.21" data-v2="1" data-v3="1" data-match="81256128" data-id="idari_3b" data-live="b1">
                        <b class="value_js"><span id="googleStatKef">1.21</span></b>
                    </span>
                    <!--b>1.21</b-->
                </span>
                &nbsp;
            </nobr>
             <nobr>
                <span class="googleStatIssue">
                    <span class="googleStatIssueName">Х2</span> -&nbsp;&nbsp;
                    <span id="koefs_idari_3b" class="bet_sel koefs" data-cnt="1" data-select="idari_3b" data-legacy="idari_3b" data-v1="1.14" data-v2="1" data-v3="1" data-match="81256128" data-id="idari_3b" data-live="b1">
                        <b class="value_js"><span id="googleStatKef">1.14</span></b>
                    </span>
                    <!--b>1.14</b-->
                </span>
                &nbsp;
            </nobr>
            <nobr>
                <span class="googleStatIssue">
                    <span class="googleStatIssueName">Ф1(1)</span> -&nbsp;&nbsp;
                    <span id="koefs_idari_3b" class="bet_sel koefs" data-cnt="1" data-select="idari_3b" data-legacy="idari_3b" data-v1="1" data-v2="1.97" data-v3="1" data-match="81256128" data-id="idari_3b" data-live="b1">
                        <b class="value_js"><span id="googleStatKef">1.97</span></b>
                    </span>
                    <!--b>1.97</b-->
                </span>
                &nbsp;
            </nobr>
            <nobr>
                <span class="googleStatIssue">
                    <span class="googleStatIssueName">Ф2(-1)</span> -&nbsp;&nbsp;
                    <span id="koefs_idari_3b" class="bet_sel koefs" data-cnt="1" data-select="idari_3b" data-legacy="idari_3b" data-v1="-1" data-v2="1.84" data-v3="1" data-match="81256128" data-id="idari_3b" data-live="b1">
                        <b class="value_js"><span id="googleStatKef">1.84</span></b>
                    </span>
                    <!--b>1.84</b-->
                </span>
                &nbsp;
            </nobr>
            <nobr>
                <span class="googleStatIssue">
                    <span class="googleStatIssueName">Тот(2.5)</span> М -&nbsp;&nbsp;
                    <span id="koefs_idari_3b" class="bet_sel koefs" data-cnt="1" data-select="idari_3b" data-legacy="idari_3b" data-v1="2.5" data-v2="2.3" data-v3="1.62" data-match="81256128" data-id="idari_3b" data-live="b1">
                        <b class="value_js"><span id="googleStatKef">2.3</span></b>
                    </span>
                    <!--b>2.3</b-->
                    &nbsp;Б -&nbsp;&nbsp;
                    <span id="koefs_idari_3b" class="bet_sel koefs" data-cnt="1" data-select="idari_3b" data-legacy="idari_3b" data-v1="2.5" data-v2="2.3" data-v3="1.62" data-match="81256128" data-id="idari_3b" data-live="b1">
                        <b class="value_js"><span id="googleStatKef"> 1.62</span></b>
                    </span>
                    <!--b>1.62</b-->
                </span>
                &nbsp;
            </nobr>
            <!-- Other nobr elements -->
        </div>
    </td>
</tr>
"""
# soup = BeautifulSoup(html_content, 'html.parser')
bets = soup.find_all('span', class_='googleStatIssue')
results = []
for bet in bets:
    name = bet.find('span', class_='googleStatIssueName').text.strip()
    value = bet.find('span', id='googleStatKef').text.strip()
    results.append((name, value))

for name, value in results:
    print(f"{name}: {value}")


from __init__ import first
import os


def main():
    color = ["red","green","yellow","black"]

    os.remove('/home/sumit/personal files/codedocu/codedocu/doc2.html')
    with open('/home/sumit/personal files/codedocu/codedocu/doc2.html', 'w+') as f:
        f.write('<html>')
        f.write('<body>')
        f.write('<table border=1px;>')
        f.write('<tr><td style="background-color:red; text-align:center"> <b>FILE NAME</b> </td> <td style="text-align: center"><b>COMMENT VALUE</b></td> </tr>')

        s = '1234567890'
        for k, v in first().iteritems():
            doc = ''
            for x, y in v.iteritems():
                try:
                    doc += y
                    #f.write('<p>%s</p>     :          %s' %(k,doc))
                except:
                    pass
            f.write('<tr><td style=background-color:red><font style="background-color:red">%s</td>:<td>%s</td>' %(k,doc.replace('"""', '')))
        for i in range(0, len(s), 60):
            f.write('<tr><td>%04d</td>' % (i+1));
        for j, k in enumerate(s[i:i+60]):
            f.write('<td><font style="background-color:%s;">%s<font></td>' % (color[j %len(color)], k));

        f.write("<b>ALPS CODE DOCUMENTATION RELEASE VERSION - 0.4.5</b>")
        f.write('<br><br>')
        f.write('</tr>')
        f.write('</table>')
        f.write('</body>')
        f.write('</html>')
        return "your code has been documented, check the html report generated."
#if __name__=='__main__':
#    main()

from __init__ import first
import os


def main():

    os.remove('/home/sumit/personal files/codedocu/codedocu/doc2.html')
    with open('/home/sumit/personal files/codedocu/codedocu/doc2.html', 'w+') as f:
        f.write('<html>')
        f.write('<body>')

        f.write("<b>ALPS CODE DOCUMENTATION RELEASE VERSION - 0.4.5</b>")
        f.write('<table border=1px;>')
        f.write('<tr><td style="background-color:red; text-align:center"> <b>FILE NAME</b> </td> <td style="text-align: center"><b>API NAME</b></td><td><b>COMMENT VALUE</b></td> </tr>')

        for k, v in first().iteritems():
            for key in v.keys():
                f.write('<tr><td style=background-color:red><font style="background-color:red">%s</td><td>%s</td><td>%s</td>' %(k,key, v[key]))

        f.write('<br><br>')
        f.write('</tr>')
        f.write('</table>')
        f.write('</body>')
        f.write('</html>')
        print "your code has been documented, check the html report generated."
if __name__=='__main__':
    print main()

<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <head>
                <meta charset='utf-8' http-equiv="Content-Type" content="text/html"/>
                <title>Solar System planets</title>
            </head>
            <body>
                <table border="1">
                    <tbody>
                        <xsl:for-each select="solar_system_planets/planet">
                            <tr>
                                <th>
                                    <xsl:value-of select="@id"/>
                                </th>
                                <th>
                                    <xsl:value-of select="name"/>
                                </th>
                                <th>
                                    <br/>
                                    <xsl:value-of select="size"/>
                                </th>
                                <xsl:for-each select="satellites">
                                    <tr>
                                        <th>
                                            Satellite
                                            <xsl:value-of select="@id_s"/>
                                        </th>
                                        <th>
                                            <xsl:value-of select="name_s"/>
                                        </th>
                                        <th>
                                            <xsl:value-of select="size_s"/>
                                        </th>
                                    </tr>
                                </xsl:for-each>
                            </tr>
                        </xsl:for-each>
                    </tbody>
                </table>
                <div id="elem1">f</div>
                <script>
<!--                    let ws = new WebSocket("ws://localhost:10556/ws");-->
<!--                    ws.onmessage = ({data}) => {-->
<!--                    jsmsg = JSON.parse(data)-->
<!--                    document.getElementById('elem1').innerHTML = jsmsg.data;-->
<!--                    }-->
<!--                    console.log('f');-->
<!--                    msg = JSON.stringify({data: "hello"} );-->
<!--                    ws.onopen = () => ws.send(msg);-->
                    let ws = new WebSocket("ws://localhost:10556/ws");
                    let msg, now;
                    ws.onmessage = function({data}) {
                    jsmsg = JSON.parse(data)
                    document.getElementById('elem1').innerHTML = jsmsg.data;
                    now = new Date();
                    msg = JSON.stringify({data: "Your message was received. My time - " + now} );
                    ws.send(msg)
                    }
                </script>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>




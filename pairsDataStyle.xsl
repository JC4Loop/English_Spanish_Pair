<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<html>
			<body>
				<h3>Spanish English Pairs</h3>
				<table>
					<tr>
						<th>Spanish</th>
						<th>Englsih</th>
					</tr>
					<xsl:for-each select="EspEngData/word">
						<tr>
							<td>
								<xsl:value-of select="spanish" />
							</td>
							<td>
								<xsl:value-of select="english" />
							</td>
						</tr>
					</xsl:for-each>
				</table>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>


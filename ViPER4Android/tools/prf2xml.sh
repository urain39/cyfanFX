if [ $# -lt 1 ]; then
	echo "Usage: $0 <prffile>"
	exit 1
fi

awk -F= '
BEGIN {
	printf "<?xml version=\x271.0\x27 encoding=\x27utf-8\x27 standalone=\x27yes\x27 ?>\n<map>\n"
}

{
	if ($2 == "string") {
		printf "    <string name=\"%s\">%s</string>\n", $1, $3
	} else if ($2 == "boolean") {
		printf "    <boolean name=\"%s\" value=\"%s\" />\n", $1, $3
	}
}

END {
	printf "</map>\n"
}
' $1

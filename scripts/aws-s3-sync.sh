
echo "starting sync"
/usr/local/bin/aws s3 sync ~/<folder> http://s3://<bucket>
echo "done!"

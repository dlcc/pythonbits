#!/bin/python
import boto.ec2.autoscale
import boto.ec2.elb
import sys

region = boto.utils.get_instance_metadata()['placement']['availability-zone'][:-1]
inst_id = boto.utils.get_instance_metadata()['instance-id']

ec2_conn = boto.ec2.connect_to_region(region)
autoscale_conn = boto.ec2.autoscale.connect_to_region(region)

asgs = []
rs = autoscale_conn.get_all_groups(next_token=None)
asgs.extend(rs)
while rs.next_token:
    rs = autoscale_conn.get_all_groups(next_token=rs.next_token)
    asgs.extend(rs)

for asg in asgs:
    for x in asg.instances:
        if x.instance_id == inst_id:
            my_asg=asg
            brethren_ids = []
            for instance in asg.instances:
                brethren_ids.append(instance.instance_id)
            brethren_ids.sort()
            if brethren_ids[0] == inst_id:
                sys.exit(0)

sys.exit(1)

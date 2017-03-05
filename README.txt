##Welcome to the Cognia Splunk Event Receiver

This application is to demonstrate the use of the Cognia Application Framework and how it can be used to send events to event reporting and alerting systems to drive realtime intelligence and auditing of recording and compliance events spanning all communications intelligence across:

* Mobile
* On Premise Fixed Line
* Hosted PBX
* Email 
* SMS/MMS/BBM/IM
* Social media events and enterprise document management systems.

In this release the following events are supported:

* Call Events (Call Made, Call Complete, Duration)
* Media Storage Events (Device, Type, Date, Size, Totals)
* Media Tagging Events (Tags created/deleted, Tags applied/removed)
* Legal Hold Events (Legal Holds created/deleted, Legal Holds applied/removed)
* Person Auditing (Users created/deleted/updated)
* Device Auditing (Devices added/deleted, Devices enabled/disabled)

The application uses the Splunk HTTP Event Collector, and works in tandem with the Cognia Event Connector from the Cognia App Store.

For details on enabling this application or the Cognia Application Framework, please contact your account manager.

###Installation & Configuration

This application uses the Splunk HTTP Event Collector.

You will need to configure a data input on a TCP port of your choice (TLS recommended). The application expects a source type of ‘cognia:event’, however if you have a naming format for your data inputs, you can use source type renaming to apply a secondary source type name.

Once your Splunk installation is configured, and you have generated a Splunk authentication token you can enable the Cognia Event Connector application via the Cognia Console and provide details of your Splunk Endpoint, TCP Port and authentication token to enable publishing of events to your Splunk Forwarder.

For assistance configuring your environment contact support@cognia.com or your Cognia reseller.

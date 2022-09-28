let details = [
  [],
  [
    "16 Jul 2021\n11:12 AM",
    "Network Update",
    "Shipment delivered Delivered, received by OLOUTOYA",
  ],
  ["16 Jul 2021\n10:05 AM", "Network Update", "Shipment is out for delivery"],
  [
    "15 Jul 2021\n10:28 PM",
    "Network Update",
    "Shipment arrived at Aramex sorting hub - in transit - will keep moving to reach its final destination country",
  ],
  [
    "15 Jul 2021\n10:27 PM",
    "Network Update",
    "Shipment arrived at Aramex sorting hub - in transit - will keep moving to reach its final destination country",
  ],
  [
    "15 Jul 2021\n01:40 PM",
    "London, United Kingdom",
    "Shipment arrived at Aramex destination facility - will be updated once ready for collection/delivery",
  ],
  [
    "14 Jul 2021\n05:31 PM",
    "Victoria Island , Nigeria",
    "Shipment departed origin country - in flight to destination",
  ],
  [
    "14 Jul 2021\n09:04 AM",
    "Victoria Island , Nigeria",
    "Shipment received at Aramex origin sorting facility",
  ],
];

let records = [];
let data = {};
let date = {};
let stamp = {};
let dayFull = {};

details.shift();

function groupDataByDate(data) {
  return data.reduce((acc, items, i) => {
    let [timestamp, location, statusInfo] = items;
    let [date, time] = timestamp.split("\n");

    if (acc[date]) {
      acc[date].records.push({
        locationStatus: `${time} Local time | ${statusInfo}`,
        currentLocation: `Service Area: ${location}`,
      });

      return acc;
    }

    acc[date] = {};
    acc[date].records = [];

    acc[date].dateStr = date;
    acc[date].records.push({
      locationStatus: `${time} Local time | ${statusInfo}`,
      currentLocation: `Service Area: ${location}`,
    });

    return acc;
  }, {});
}
details = groupDataByDate(details);
details = Object.entries(details).map(([key, { dateStr, records }], i) => {
  date = new Date(dateStr);
  dayFull = date.toLocaleString("en-GB", { weekday: "long" });
  stamp = new Intl.DateTimeFormat("en-GB", { dateStyle: "long" }).format(date);

  data["item" + i] = {
    day: dayFull,
    stamp,
    records,
  };
});

// details.map((detail, index) => {
//   if (detail.length) {
//     let [dayString, location, status] = detail;
//     let [dateStr, time] = dayString.split("\n");

//     date = new Date(dateStr);
//     dayFull = date.toLocaleString("en-GB", { weekday: "long" });
//     stamp = new Intl.DateTimeFormat("en-GB", { dateStyle: "long" }).format(
//       date
//     );

//     console.log({
//       day: dayFull,
//       stamp: dateStr,
//       records: {
//         locationStatus: `${time} Local Time | ${status}`,
//         currentLocation: `Service Area: ${location}`,
//       },
//     });
//     data["item" + index] = {
//       day: dayFull,
//       stamp: dateStr,
//       records: {
//         locationStatus: `${time} Local Time | ${status}`,
//         currentLocation: `Service Area: ${location}`,
//       },
//     };
//   }
// });

console.log("DATA: ", data);

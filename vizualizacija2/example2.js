// učitavanje podataka u json formatu
/*d3.json("http://127.0.0.1:5000/stats", function(_error, data) {

    data.forEach(function(d) {
        d.vendor = d.vendor;
    });
})*/

const getJSON = async url => {
    try {
      const response = await fetch(url);
      if(!response.ok) // check if response worked (no 404 errors etc...)
        throw new Error(response.statusText);
  
      const data = await response.json(); // get JSON from the response
      return data; // returns a promise, which resolves to this data value
    } catch(error) {
      return error;
    }
  }

var stats = getJSON("http://127.0.0.1:5000/stats").then(data => {
  stats = data;
}).catch(error => {
  console.error(error);
});

 /* console.log("Fetching data...");
  getJSON("http://127.0.0.1:5000/stats").then(data => {
    stats = data;
    //console.log(data);
  }).catch(error => {
    console.error(error);
  });*/
    
var tasks = [

    {
        "startDate" : new Date(new Date() - new Date(24 * 60 * 60 * 1000)),
        "endDate" : new Date(),
        "taskName" : "E Job", "status" : "RUNNING"
    }
    
    ];
    
    var taskStatus = {
        "SUCCEEDED" : "bar",
        "FAILED" : "bar-failed",
        "RUNNING" : "bar-running",
        "KILLED" : "bar-killed"
    };
    
 

    var i;
    for (i = 0; i < stats.data[i].length; i++) {
      i++;
    }

    var vendor = [ "D Job", "P Job", "E Job", "A Job", "N Job" ];
    
    tasks.sort(function(a, b) {
        return a.endDate - b.endDate;
    });

    var maxDate = tasks[tasks.length - 1].endDate;
    tasks.sort(function(a, b) {
        return a.startDate - b.startDate;
    });
    var minDate = tasks[0].startDate;
    
    var format = "%H:%M";
    
    var gantt = d3.gantt().taskTypes(vendor).taskStatus(taskStatus).tickFormat(format);
    //gantt.timeDomain([new Date("Sun Dec 09 04:54:19 EST 2012"),new Date("Sun Jan 09 04:54:19 EST 2013")]);
    //gantt.timeDomainMode("fixed");
    gantt(tasks);
    
    
    function addTask() {
        
        var lastEndDate = Date.now();
        if (tasks.length > 0) {
        lastEndDate = tasks[tasks.length - 1].endDate;
        }
        
        var taskStatusKeys = Object.keys(taskStatus);
        var taskStatusName = taskStatusKeys[Math.floor(Math.random()*taskStatusKeys.length)];
        var taskName = vendor[Math.floor(Math.random()*vendor.length)];
        
        tasks.push({"startDate":d3.time.hour.offset(lastEndDate,Math.ceil(1*Math.random())),"endDate":d3.time.hour.offset(lastEndDate,(Math.ceil(Math.random()*3))+1),"taskName":taskName,"status":taskStatusName});
        gantt.redraw(tasks);
    };
    
    function removeTask() {
        tasks.pop();
        gantt.redraw(tasks);
    };
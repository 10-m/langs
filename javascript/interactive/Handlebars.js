// Using Handlebars expressions
{
  const source = document.getElementById('greet').innerHTML;
  const template = Handlebars.compile(source);
  const context = {
    greeting: 'Hello World!'
  };
  const compiledHtml = template(context);
  const fill = document.getElementById('hello');
  fill.innerHTML = compiledHtml;
}

// Handlebars "If" block helper
{
  const source = document.getElementById('ifHelper').innerHTML;
  const template = Handlebars.compile(source);
  const context = {
    opinion: true
  };
  const compiledHtml = template(context);
  const debateElement = document.getElementById('debate');
 debateElement.innerHTML = compiledHtml;
}

// Handlebars "Else" section
{
  const source = document.getElementById('ifelseHelper').innerHTML;
  const template = Handlebars.compile(source);

  let context = {
    opinion: false
  };
  const compiledHtml = template(context);
  const debateElement = document.getElementById('debate2');
  debateElement.innerHTML = compiledHtml;
}

// Handlebars "Each" and "This" - Part I 
{
  const source = document.getElementById('eachHelper').innerHTML;
  const template = Handlebars.compile(source);

  const context = {
    newArray: [...Array(10).keys()].map(i => ++i)
  };

  const compiledHtml = template(context);
  const displayElements = document.getElementById('display');
  displayElements.innerHTML = compiledHtml;
}

// Handlebars "Each" and "This" - Part II
{
  const source = document.getElementById('languagesTemp').innerHTML;
  const template = Handlebars.compile(source);

  const context = {
    languages: [
      {name: 'HTML'}, 
      {name: 'CSS'}, 
      {name: 'JavaScript'}
    ]
  };
  const compiledHtml = template(context);
  const displayGoals = document.getElementById('goals');
  displayGoals.innerHTML = compiledHtml;
}

// Combining "If" and "Each"
{
  const source = document.getElementById('languagesTemp2').innerHTML;
  const template = Handlebars.compile(source);

  const context = {
    languages: [
      {
        name: 'HTML',
        modern: true
      },
      {
        name:'CSS',
        modern: true
      }, 
      {
        name: 'JavaScript',
        modern: true
      },
      {
        name: 'COBOL',
        modern: false
      }
    ]
  };

  const compiledHtml = template(context);
  const displayGoals = document.getElementById('goals2');
  displayGoals.innerHTML = compiledHtml;
}

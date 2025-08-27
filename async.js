const functionName = async (arg1, arg2) => {
    console.log("Hello");

    await new Promise(resolve => {
        setTimeout(() => {
            console.log("Inside the setTimeout");
            resolve();
        }, 2000);
    });

    console.log("Hello 2");
};

await functionName("arg1", "arg2");
console.log("Outside of the function");
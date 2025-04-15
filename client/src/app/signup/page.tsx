import Image from "next/image";
import Link from "next/link";
import React from "react";

function page() {
  return (
    <div className="overflow-x-hidden">
      <div className="flex-row w-xl md:flex bg-blue-100 md:w-5xl h-[600px] md:mt-28 md:ml-52 rounded-3xl ">
        <div className=" ">
          <Image
            width={500}
            height={500}
            className=" size-fit rounded-sm -ml-32  md:ml-10 md:mt-28 md:rounded-4xl md:mb-6 md:cover"
            src="/signup.png"
            alt="image"
          ></Image>
        </div>
        <div className=" ml-6 md:ml-28 mt-28">
          <h1 className=" ml-9 font-bold text-2xl">Create An Account</h1>
          <h4 className="mt-12 text-lg">Username</h4>
          <input type="text" className="rounded-3xl bg-white h-10 w-56 mt-2" />
          <h4 className="mt-10 text-lg">Password</h4>
          <input
            type="password"
            className="rounded-3xl bg-white h-10 w-56 mt-2"
          />
          <br />
          <button className="bg-yellow-100 mt-8 text-lg w-32 rounded-lg h-10">
            SignUp
          </button>
          <Link href="/signin">
            <h5 className="text-sm mt-1">Already have an account?SignIn</h5>
          </Link>
        </div>
      </div>
    </div>
  );
}

export default page;

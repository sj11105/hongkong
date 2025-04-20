"use client";

import { useState } from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Checkbox } from "@/components/ui/checkbox";
import {
  AudioWaveformIcon as Waveform,
  ArrowRight,
  Eye,
  EyeOff,
  Check,
  Info,
} from "lucide-react";
import { motion } from "framer-motion";

export default function SignUp() {
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [password, setPassword] = useState("");

  // Password strength indicators
  const hasMinLength = password.length >= 8;
  const hasUppercase = /[A-Z]/.test(password);
  const hasNumber = /[0-9]/.test(password);
  const hasSpecialChar = /[^A-Za-z0-9]/.test(password);

  return (
    <div className="flex min-h-screen flex-col bg-white">
      <div className="container flex h-16 items-center">
        <Link href="/" className="flex items-center gap-2">
          <Waveform className="h-6 w-6 text-teal-500" />
          <span className="text-xl font-bold bg-gradient-to-r from-teal-500 to-emerald-500 bg-clip-text text-transparent">
            VoiceScript
          </span>
        </Link>
      </div>

      <div className="flex-1 flex items-center justify-center py-12">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="w-full max-w-md px-4"
        >
          <Card className="border-slate-200 shadow-lg overflow-hidden">
            <div className="h-2 bg-gradient-to-r from-teal-500 to-emerald-500"></div>
            <CardHeader className="space-y-1 pt-6">
              <CardTitle className="text-2xl font-bold text-center">
                Create an account
              </CardTitle>
              <CardDescription className="text-center">
                Enter your information to create your account
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-4 pt-4">
              <div className="grid grid-cols-2 gap-4">
                <div className="space-y-2">
                  <Label htmlFor="first-name">First Name</Label>
                  <Input
                    id="first-name"
                    placeholder="John"
                    className="border-slate-200 focus-visible:ring-teal-500"
                  />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="last-name">Last Name</Label>
                  <Input
                    id="last-name"
                    placeholder="Doe"
                    className="border-slate-200 focus-visible:ring-teal-500"
                  />
                </div>
              </div>

              <div className="space-y-2">
                <Label htmlFor="username">Username</Label>
                <Input
                  id="username"
                  placeholder="johndoe"
                  className="border-slate-200 focus-visible:ring-teal-500"
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="email">Email</Label>
                <Input
                  id="email"
                  type="email"
                  placeholder="john.doe@example.com"
                  className="border-slate-200 focus-visible:ring-teal-500"
                />
              </div>

              <div className="space-y-2">
                <Label htmlFor="password">Password</Label>
                <div className="relative">
                  <Input
                    id="password"
                    type={showPassword ? "text" : "password"}
                    placeholder="Create a password"
                    className="border-slate-200 focus-visible:ring-teal-500 pr-10"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                  />
                  <button
                    type="button"
                    onClick={() => setShowPassword(!showPassword)}
                    className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600"
                  >
                    {showPassword ? <EyeOff size={18} /> : <Eye size={18} />}
                  </button>
                </div>

                {password && (
                  <div className="mt-2 space-y-2">
                    <p className="text-xs font-medium text-slate-500">
                      Password requirements:
                    </p>
                    <ul className="space-y-1 text-xs">
                      <li className="flex items-center gap-1">
                        <span
                          className={`flex h-4 w-4 items-center justify-center rounded-full ${
                            hasMinLength
                              ? "bg-emerald-100 text-emerald-600"
                              : "bg-slate-100 text-slate-400"
                          }`}
                        >
                          {hasMinLength ? (
                            <Check size={10} />
                          ) : (
                            <Info size={10} />
                          )}
                        </span>
                        <span
                          className={
                            hasMinLength ? "text-emerald-600" : "text-slate-500"
                          }
                        >
                          At least 8 characters
                        </span>
                      </li>
                      <li className="flex items-center gap-1">
                        <span
                          className={`flex h-4 w-4 items-center justify-center rounded-full ${
                            hasUppercase
                              ? "bg-emerald-100 text-emerald-600"
                              : "bg-slate-100 text-slate-400"
                          }`}
                        >
                          {hasUppercase ? (
                            <Check size={10} />
                          ) : (
                            <Info size={10} />
                          )}
                        </span>
                        <span
                          className={
                            hasUppercase ? "text-emerald-600" : "text-slate-500"
                          }
                        >
                          At least one uppercase letter
                        </span>
                      </li>
                      <li className="flex items-center gap-1">
                        <span
                          className={`flex h-4 w-4 items-center justify-center rounded-full ${
                            hasNumber
                              ? "bg-emerald-100 text-emerald-600"
                              : "bg-slate-100 text-slate-400"
                          }`}
                        >
                          {hasNumber ? <Check size={10} /> : <Info size={10} />}
                        </span>
                        <span
                          className={
                            hasNumber ? "text-emerald-600" : "text-slate-500"
                          }
                        >
                          At least one number
                        </span>
                      </li>
                      <li className="flex items-center gap-1">
                        <span
                          className={`flex h-4 w-4 items-center justify-center rounded-full ${
                            hasSpecialChar
                              ? "bg-emerald-100 text-emerald-600"
                              : "bg-slate-100 text-slate-400"
                          }`}
                        >
                          {hasSpecialChar ? (
                            <Check size={10} />
                          ) : (
                            <Info size={10} />
                          )}
                        </span>
                        <span
                          className={
                            hasSpecialChar
                              ? "text-emerald-600"
                              : "text-slate-500"
                          }
                        >
                          At least one special character
                        </span>
                      </li>
                    </ul>
                  </div>
                )}
              </div>

              <div className="space-y-2">
                <Label htmlFor="confirm-password">Confirm Password</Label>
                <div className="relative">
                  <Input
                    id="confirm-password"
                    type={showConfirmPassword ? "text" : "password"}
                    placeholder="Confirm your password"
                    className="border-slate-200 focus-visible:ring-teal-500 pr-10"
                  />
                  <button
                    type="button"
                    onClick={() => setShowConfirmPassword(!showConfirmPassword)}
                    className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600"
                  >
                    {showConfirmPassword ? (
                      <EyeOff size={18} />
                    ) : (
                      <Eye size={18} />
                    )}
                  </button>
                </div>
              </div>

              <div className="flex items-start space-x-2">
                <Checkbox id="terms" className="mt-1" />
                <Label
                  htmlFor="terms"
                  className="text-sm font-normal leading-tight"
                >
                  I agree to the{" "}
                  <Link
                    href="/terms"
                    className="font-medium text-teal-600 hover:text-teal-700 underline-offset-4 hover:underline"
                  >
                    Terms of Service
                  </Link>{" "}
                  and{" "}
                  <Link
                    href="/privacy"
                    className="font-medium text-teal-600 hover:text-teal-700 underline-offset-4 hover:underline"
                  >
                    Privacy Policy
                  </Link>
                </Label>
              </div>

              <Button className="w-full bg-gradient-to-r from-teal-500 to-emerald-500 hover:from-teal-600 hover:to-emerald-600">
                Create Account
                <ArrowRight className="ml-2 h-4 w-4" />
              </Button>
            </CardContent>
          </Card>
        </motion.div>
      </div>
    </div>
  );
}

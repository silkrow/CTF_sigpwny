undefined4 main(int param_1,long param_2)

{
  size_t sVar1;
  int local_3c;
  undefined8 local_38;
  undefined8 local_30;
  undefined8 local_28;
  undefined4 local_20;
  undefined2 local_1c;
  undefined local_1a;
  long local_18;
  int local_10;
  undefined4 local_c;
  
  local_c = 0;
  local_18 = param_2;
  local_10 = param_1;
  if (param_1 < 2) {
    puts("Usage: ./angry flag\nFlag is ascii with the format sigpwny{...}");
    local_c = 1;
  }
  else {
    sVar1 = strlen(*(char **)(param_2 + 8));
    if (sVar1 == 0x1f) {
      s2206376623(*(undefined8 *)(local_18 + 8));
      s3880481467(*(undefined8 *)(local_18 + 8));
      s345299474(*(undefined8 *)(local_18 + 8));
      s373069732(*(undefined8 *)(local_18 + 8));
      s3278859051(*(undefined8 *)(local_18 + 8));
      s493285452(*(undefined8 *)(local_18 + 8));
      s3088440140(*(undefined8 *)(local_18 + 8));
      s2319860955(*(undefined8 *)(local_18 + 8));
      s1343118312(*(undefined8 *)(local_18 + 8));
      s1994491177(*(undefined8 *)(local_18 + 8));
      s2477169866(*(undefined8 *)(local_18 + 8));
      s3306800787(*(undefined8 *)(local_18 + 8));
      s2030153530(*(undefined8 *)(local_18 + 8));
      s75927662(*(undefined8 *)(local_18 + 8));
      s1476774293(*(undefined8 *)(local_18 + 8));
      s2172966575(*(undefined8 *)(local_18 + 8));
      local_38 = 0x858712997682b1b4;
      local_30 = 0xdae67b2d46152991;
      local_28 = 0x8fb3a7e55077d4c3;
      local_20 = 0xfaec4847;
      local_1c = 0xcbd9;
      local_1a = 0x25;
      for (local_3c = 0; local_3c < 0x1f; local_3c = local_3c + 1) {
        if (*(char *)(*(long *)(local_18 + 8) + (long)local_3c) !=
            *(char *)((long)&local_38 + (long)local_3c)) {
          puts("That flag is incorrect.");
          return 0;
        }
      }
      puts("That flag is correct! Congrats.");
      local_c = 0;
    }
    else {
      puts("That flag is incorrect.");
      local_c = 0;
    }
  }
  return local_c;
}
